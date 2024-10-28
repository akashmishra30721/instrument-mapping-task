# instrument-mapping-task

Each broker provides a file containing a list of instruments they support. However, the same instrument might have different names across brokers, and identifiers (IDs) are unique to each broker. For example, "Reliance Industries" might appear as "RELIANCE IND" in one broker’s data and "REL INDUST" in another’s.

The main objective of this project is to create a unified mapping of financial instruments across multiple brokers—Kotak, Fyers, Angel One, and Zerodha. Each broker provides a unique identifier for the financial instruments they support, and this project aims to consolidate these IDs into a single table with accurate mappings.

Steps Involved
1. Data Loading and Preprocessing:
Load the instrument data files for Kotak, Fyers, Angel One, and Zerodha.
Standardize and clean Instrument Name columns by removing extra spaces and converting to uppercase.
2. Merging on ISIN:
Perform an outer merge on the ISIN column to join Kotak and Fyers data.
Filter out rows with missing ISIN values to avoid false matches.
3. TF-IDF Vectorization and Cosine Similarity:
Use TF-IDF vectorization to create embeddings for instrument names.
Calculate cosine similarity to find the best match for Angel One and Zerodha instrument names.
Set a threshold to ensure accurate matches.
4. Filtering Results:
Organize columns in the order: Instrument Name, Kotak ID, Fyers ID, Angel One ID, Zerodha ID.
5. Save the final output as an csv file

For this project,<br>
<i>kotak.csv, angelone.csv, fyers,csv</i> and <i> zerodha.csv</i> are the input files on which we perform the task. <br>
The task of data collection can be found in <i>data collection.ipynb</i><br>
<i>final_mapping.ipynb</i> contains the final task.<br>
The final output can be vieed in <i>final_mapping.csv</i>


