"""
OECD API Client voor Data Structures and Algorithms project
Deze module biedt functies om data op te halen via de OECD SDMX API
"""

import requests
import pandas as pd
from typing import Optional, Dict, List


class OECDAPIClient:
    """Client voor OECD SDMX API"""
    
    def __init__(self):
        self.base_url = "https://sdmx.oecd.org/public/rest"
        self.archive_url = "https://sdmx.oecd.org/archive/rest"
    
    def get_data(self, 
                 agency: str = "OECD",
                 dataset: str = "DF_GENDER_EMP",
                 version: str = "",
                 data_selection: str = "all",
                 start_period: Optional[str] = None,
                 end_period: Optional[str] = None,
                 format: str = "csv") -> pd.DataFrame:
        """
        Haal data op via OECD API
        
        Args:
            agency: Agency identifier (default: OECD)
            dataset: Dataset identifier (default: DF_GENDER_EMP)
            version: Dataset version (leeg voor laatste versie)
            data_selection: Data selectie (default: all voor alles)
            start_period: Start periode (bijv: "2020", "2020-Q1")
            end_period: Eind periode (bijv: "2023", "2023-Q4")
            format: Response format (csv, jsondata, genericdata)
        
        Returns:
            DataFrame met de opgehaalde data
        """
        # Bouw URL
        url = f"{self.archive_url}/data/{agency},{dataset}"
        if version:
            url += f"@{version}"
        url += f"/{data_selection}"
        
        # Voeg parameters toe
        params = {}
        if format:
            params["format"] = format
        if start_period:
            params["startPeriod"] = start_period
        if end_period:
            params["endPeriod"] = end_period
        
        # Haal data op
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        # Parse response
        if format == "csv":
            from io import StringIO
            return pd.read_csv(StringIO(response.text))
        elif format == "jsondata":
            import json
            data = response.json()
            # JSON parsing zou hier geïmplementeerd moeten worden
            return pd.DataFrame(data)
        else:
            raise ValueError(f"Format {format} nog niet geïmplementeerd")
    
    def get_structure(self, 
                     agency: str = "OECD",
                     dataset: str = "DF_GENDER_EMP",
                     version: str = "") -> Dict:
        """
        Haal data structuur op (metadata, dimensies, etc.)
        
        Args:
            agency: Agency identifier
            dataset: Dataset identifier
            version: Dataset version
        
        Returns:
            Dictionary met structuur informatie
        """
        url = f"{self.archive_url}/dataflow/{agency},{dataset}"
        if version:
            url += f"@{version}"
        
        params = {
            "references": "all",
            "detail": "referencepartial"
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def get_filtered_data(self,
                         country: str = "USA",
                         gender: str = "WOMEN",
                         age_group: str = "25-54",
                         start_year: str = "2020",
                         end_year: str = "2023") -> pd.DataFrame:
        """
        Haal gefilterte data op met specifieke parameters
        
        Args:
            country: Land code (bijv: USA, NLD, DEU)
            gender: Gender (MEN, WOMEN, ALL_PERSONS)
            age_group: Leeftijdsgroep (15-24, 25-54, 55-64, etc.)
            start_year: Start jaar
            end_year: Eind jaar
        
        Returns:
            DataFrame met gefilterde data
        """
        # Map leeftijdsgroepen naar OECD codes
        age_mapping = {
            "15-24": "1524",
            "25-54": "2554", 
            "55-64": "5564",
            "55+": "55PLUS",
            "15+": "15PLUS"
        }
        
        age_code = age_mapping.get(age_group, age_group)
        
        # Bouw data selection string - volgens SDMX syntax: COU.SEX.AGE
        data_selection = f"{country}.{gender}.{age_code}"
        
        try:
            return self.get_data(
                data_selection=data_selection,
                start_period=start_year,
                end_period=end_year,
                format="csv"
            )
        except Exception as e:
            print(f"API error met gefilterde query: {e}")
            print("Poging met alternatieve methode...")
            # Fallback: haal alle data en filter lokaal
            all_data = self.get_data(
                start_period=start_year,
                end_period=end_year,
                format="csv"
            )
            # Filter lokaal
            filtered = all_data[
                (all_data['COU'] == country) & 
                (all_data['SEX'] == gender) & 
                (all_data['AGE'] == age_code)
            ]
            return filtered


# Voorbeeld gebruik
if __name__ == "__main__":
    client = OECDAPIClient()
    
    # Haal alle data op
    print("Alle data ophalen...")
    all_data = client.get_data()
    print(f"Totaal aantal rijen: {len(all_data)}")
    print(f"Kolommen: {all_data.columns.tolist()}")
    
    # Haal gefilterde data op
    print("\nGefilterde data ophalen (USA, vrouwen, 25-54, 2020-2023)...")
    filtered_data = client.get_filtered_data(
        country="USA",
        gender="WOMEN", 
        age_group="25-54",
        start_year="2020",
        end_year="2023"
    )
    print(f"Gefilterde rijen: {len(filtered_data)}")
    print(filtered_data.head())
