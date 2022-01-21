import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.medicalrecord = []
        self.studentrecord = []

        self.new_block(previous_hash="hallo world", proof=100)

# Create a new block listing key/value pairs of block information in a JSON object. Reset the list of medical records and& append the newest block to the chain.

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'records': self.medicalrecord,
            'test': self.studentrecord,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.medicalrecord = []
        self.studentrecord = []
        self.chain.append(block)
          
        return block 


    @property
    def last_block(self):
 
        return self.chain[-1]

# Add a transaction with relevant info to the 'medical' - list of pending tx's. 


    def new_mrecord(self,doctorName, patientID,patientName,   procedureCode, visitDate,):
        m_records = {
            'doctorName' :doctorName,
            'patientID': patientID,
            'patientName': patientName,
            'procedureCode' : procedureCode,
            'visitDate': visitDate,            
            
            
        }
        
        y = json.dumps(m_records)
        self.medicalrecord.append(y)
        return self.last_block['index'] + 1
    
    
    
# Add a transaction with relevant info to the 'student' - list of pending tx's. 


    def new_srecord(self,studentName,courseName, studentID, studentCode, admissionDate):
        s_records = {
            'studentName' :studentName,
            'studentID': studentID,
            'courseName': courseName,           
            'studentCode' : studentCode,
            'admissionDate': admissionDate,            
            
            
        }
        
      
        self.studentrecord.append(s_records)
        return self.last_block['index'] + 1
    
    

# receive one block. Turn it into a string,

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()
        print("Hash: ", hex_hash)

        return hex_hash


blockchain = Blockchain()

t1 = blockchain.new_mrecord("dr joshef", "1234", 'Joseph Sliwka', '582', "2/21/2019")
t2 = blockchain.new_srecord("dr", "123t",'dd', 'asgasf', "2/21/2019")

blockchain.new_block(12345)

print("Genesis block: ",blockchain.chain)
