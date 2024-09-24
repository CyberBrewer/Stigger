import pandas as pd
import os

vulns = pd.read_csv("Vuln_Test_Nessus.csv")
Source = pd.read_excel("FedRAMP-POA&M-Template.xlsx")
"""Reads the Vulns and source CSV file and returns its contents as a Dataframe."""