import unittest
import DiceGame

class testDiceGame(unittest.Testcase):
    
    def test_game(self):
        result = DiceGame.game(1,1,1)
        self.assertEqual(result, 7)
        
if __name__ == '__main__':
    unittest.main()