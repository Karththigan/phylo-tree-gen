import requests 

# All E-utility calls share the same base URL
eutility_base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

# Take in list of NCBI GEN Bank numbers that user wants to compare unknown sequence 
# Here, it's in genbank_numbers.txt

# Create list of genbank numbers to pass in to url call, in the form of number1,number2, etc.
species_query = ""
with open("genbank_numbers.txt", "r") as species_file:
    for number in species_file:
        species_query += number.strip('\n') + ","
        
    species_query = species_query[:-1]  # Remove last comma


# Download FASTA file of desired species's sequences to compare to unknown sequences
e_fetch_call = f"efetch.fcgi?db=nuccore&id={species_query}&rettype=fasta&retmode=text"
efetch_call = eutility_base_url + e_fetch_call

# Get FASTA file data from sequences
response = requests.get(efetch_call)

# Write response to output FASTA file
with open("output.txt", "wb") as f:
    f.write(response.content)
