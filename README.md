# ISIEboard
Scripts for the processing of ISIE data for analysis

Here are scripts to reproduce the analysis of the membership data of the International Society for Industrial Ecology (ISIE) for the years 2021-2024. The data was obtained from the ISIE secretariat and processed to analyze different parameters. 

The environment used for the analysis is python 3.11.0 and can be installed from the isie_env.yml file using the following command:
``` bash
conda env create -f isie_env.yml
```
The packages used in the analysis are:


## Analyzing the role of IE day in membership renewal
The script `IEday_analysis.py` analyzes the role of the International Industrial Ecology Day in membership renewal. The script then plots the results in a bar chart.