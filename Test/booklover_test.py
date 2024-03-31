import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        test_object = BookLover("Victor", "qfw3cr@virginia.edu", "fantasy")
        test_object.add_book("King Kong", 4)
        self.assertIn("King Kong", test_object.book_list['book_name'].values)
        
    def test_2_add_book(self):
        test_object = BookLover("Victor", "qfw3cr@virginia.edu", "None Fiction")
        test_object.add_book("SuperNatural", 4)
        test_object.add_book("SuperNatural", 4)
        self.assertEqual(len(test_object.book_list), 1)
        
    def test_3_has_read(self): 
        test_object = BookLover("Victor", "qfw3cr@virginia.edu", "fantasy")
        test_object.add_book("King Kong", 4)
        self.assertTrue(test_object.has_read("King Kong"))
        
    def test_4_has_read(self): 
        test_object = BookLover("Victor", "qfw3cr@virginia.edu", "None Fiction")
        test_object.add_book("Fight Club", 4)
        self.assertFalse(test_object.has_read("Fight Club"))
        
    def test_5_num_books_read(self): 
        test_object = BookLover("Victor", "qfw3cr@virginia.edu", "Historical Fiction")
        test_object.add_book("Irish Man", 4)
        test_object.add_book("Pompei", 3)
        test_object.add_book("Lincoln", 5)
        self.assertEqual(test_object.num_books_read(), 3)

    def test_6_fav_books(self):
        test_object = BookLover("Victor", "qfw3cr@virginia.edu", "Fiction")
        test_object.add_book("Titans", 4)
        test_object.add_book("Star Wars", 5)
        test_object.add_book("Dune", 4)
        fav_books = test_object.fav_books()
        self.assertTrue(all(fav_books['book_rating'] > 3))

if __name__ == '__main__':
    unittest.main(verbosity=3)