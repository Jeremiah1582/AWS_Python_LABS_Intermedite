# In this lab, you will:

# Create a module
# Open a file and load the JSON data it contains using the built-in JSON module of Python
# Parse the JSON structure to access insulin data
# Calculate the rough molecular weight of human insulin using given code (similar to the lab Working with the String Sequence and Numeric Weight of Insulin in Python)

    
    # CaLCULATING THE WEIGHT------------------------------------

import fileHandler_module

data= fileHandler_module.readJsonFile('myFiles/insulin.json')

if data != "":
  #part 1  
    bInsulin = data['molecules']['bInsulin'] #NOTE: this is similar to dot notation in for objects JS- we are asking to look into DICT named MOLECULES to return Value of BINSULINE (js bInsulin = data.molecules.bInsulin)
    aInsulin = data["molecules"]['aInsulin']
    # NOTE: Method 2: TUPLE_UNPACKING/ DESTRUCTURING (js- const {x,y,z}=data.body)
    #  lsInsulin,bInsulin,aInsulin,cInsulin= data['molecules'].items()
    
    insulin = bInsulin + aInsulin
    molecularWeightInsulinActual= data['molecularWeightInsulinActual']
  #part 2
    print("bInsulin: ",bInsulin)
    print("aInsulin: ",aInsulin)
    print('molecularWeightInsulinActual: ', str(molecularWeightInsulinActual))
    
  #part 3
    # calculating the Amino Acid Weight
    aminoAcids = ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']
    aaWeight = data['weights'] # get list of weight from dictionary 
    aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in aminoAcids}) #Counts each Amino Acid in the sequence
    molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeight[x]) for x in aminoAcids}.values())
    
    print( "The rough molecular weight of insulin: ", str(molecularWeightInsulin))
    print("Percent error: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))

else:
    print('there was an')