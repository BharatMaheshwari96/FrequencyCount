import re
def CountFrequency(my_list): 
  
    # Creating an empty dictionary  
    freq = {} 
    for item in my_list: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
    print("")
    print("The frequency of all the elements of the list:")
    for key, value in freq.items(): 
        
        print ("% d occurs  % d times"%(key, value)) 
        
def main():
    Element = []
    RANGE = int(input("Input the number of elements to be stored in the list: "))
    print("Input",RANGE,"elememts in the list:")
    for i in range(RANGE):
        print("element -", i, ":",end = " ") 
        element = int(input())
        Element.append(element)
    CountFrequency(Element)
  
main()



