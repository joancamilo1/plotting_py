# plotting in seaborn and plotly
Seaborn and plotly graphics are prioritized, since the knime graphics engine is more suitable for these libraries

I am in the initial phase of the project where I have to brainstorm what is the best way to generate understandable graphics for the end user, therefore the code is not very refined. The objective is to adequately graph an engineering and data science process where the efficiency of different hospitals is studied based on the patients treated, and their associated costs.

steps prior to having the BDD
- you take a database from snowflake
- unnecessary columns are discarded and I do an initial data analysis
- DMUs are separated in each GRD
- Through a data envelopment analysis (DEA), the efficiency of each DRG is obtained, in addition to costs and target expenses (code in R)
- Finally, the analyzes are united in a BDL which is the input for the following graph
