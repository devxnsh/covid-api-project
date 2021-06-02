import csv
import json
def elementbyelement(list):
        for element in list:
            return(element)
    #returns all elements in a list. (Don't ask why)
def dictkeysshow(dict):
        keyslist = []
        keys = dict.keys()
        for dictkey in keys:
            keyslist.append(dictkey)
    #appends all keys of a dictionary in a list.
        return(keyslist)
def dictvaluesshow(dict):
        valueslist = []
        values = dict.values()
        for dictvalue in values:
            valueslist.append(dictvalue)
        return(valueslist)
    #appends all values of a dictionary in a list.
def save_slots():
    fh1=open("session_details.csv","w")
    wobj1=csv.writer(fh1)
    fh2=open("data_head.csv","w")
    wobj=csv.writer(fh2)
    
    keys = []
    values_list= valueslist = []
    with open ("somefiles.json", "r") as fh:
        
        readerjson=json.load(fh)
        fh.close() #loads the json file which was created in tracker.
    for i in readerjson: #one layer into the json
        for j in readerjson[i]: #two layers into the json
            keys = dictkeysshow(j)
            if len(keys) ==14  :
                keys.pop() #the creators of the object input a "vaccine-cost" element in the list 
                            #whose position could not be formulated, neither was it useful in our prog.
            keys.pop() #they also inserted a "sessions" json object nested into the big json object,
                       # which was a little too big to be accomodated in the primary csv file.
            wobj.writerow(keys)
            
            break
    for i in readerjson:
        for j in readerjson[i]:
            values_list = []
            values = j.values()
            for i in values :
                values_list.append(i)
                valueslist.append(i)
            if len(values_list)==14 :
                values_list.pop()
            #values_list does not contain the sessions or the vaccine cost data, but valueslist does.
            #we will be using valueslist to write a separate file on session details.
            values_list.pop()
            wobj.writerow(values_list)
            
            

    count = 0
            
    for i in valueslist:
        
        if type(i) == list :
            if len(i[0])!=2: #the one with two elements is the one with vaccine details, hence ruling it out. 
                # Session Details contains 8 fields.
                elements = elementbyelement(i)
                #writing into session_details
                if count == 0 :
                    wobj1.writerow(dictkeysshow(elements))
                    count +=1
                wobj1.writerow(dictvaluesshow(elements))
if __name__ == "__main__":
    save_slots()
                    