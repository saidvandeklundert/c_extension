"""
pip install -e src/
python3 src/test.py
"""
import c_extension


if __name__ == "__main__":
    
    c_res = c_extension.multiplier(4, 25)    
    
    print(c_res)
    
