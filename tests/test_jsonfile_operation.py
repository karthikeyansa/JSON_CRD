from jsonfile_crd.jsonfile_operation import JsonFileOperation
from jsonfile_crd.jsonfile_helper import HelperValidator
import unittest

class Testing(unittest.TestCase):
    # json_obj is used to access methods from JsonFileOperation class
    json_obj = JsonFileOperation()
    # helper_obj is used to access methods from HelperValidator class
    helper_obj = HelperValidator()

    # To test for key is alphanum.
    def test_key_isalpha(self):
        self.assertRaises(Exception, self.helper_obj.validate_key, "data12k", "ola", 1000)
    
    # To test for key is crossing 32 bytes.
    def test_key_read(self):
        self.assertRaises(Exception, self.helper_obj.validate_key, "abcd"*40)

    # To test for given invalid filepath. 
    def test_filepath(self):
        self.assertRaises(Exception, self.helper_obj.validate_file, "/Users/karthikeyan/desktop/testing/")
    
    # To test for value is crossing 16 KB.
    def test_valuesize(self):
        self.assertRaises(Exception, self.helper_obj.validate_value, "python"*20000)

    def test_JsonFileOperation(self):
        '''
        The function test_JsonFileOperation with key, value and ttl as arguments 
        returns "data_created", "key", "data_deleted".
        '''
        self.assertEqual(self.json_obj.create_data("dataone", "this is red area with 16 people living", 1000), "data_created")
        self.assertEqual(self.json_obj.read_data("dataone"), "this is red area with 16 people living")
        self.assertEqual(self.json_obj.delete_data("dataone"), "data_deleted")

if __name__ == '__main__':
    unittest.main()