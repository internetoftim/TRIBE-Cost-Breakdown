from tribe import *

def main():                                                 

    test_input = '10 IMG 15 FLAC 13 VID'                    # Test case from documentation
    out_val = extract_breakdown(input_string=test_input)    # Call extraction from row
    for item in out_val:                                    # Display output
        print(item)    
    

main()                                          
