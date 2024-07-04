"""
Author: Jayamadu Gammune

This script implements a Hole Centering Tool using computer vision techniques.
It detects circular shapes (holes) from a webcam feed and provides visual feedback
to align these holes with a crosshair displayed on the screen.

Permission is hereby granted, free of charge, to any person obtaining a copy of 
this software and associated documentation files (the "Software"), to deal in 
the Software without restriction, including without limitation the rights to 
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies 
of the Software, and to permit persons to whom the Software is furnished to do 
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
SOFTWARE.
"""

#generate 11 random values upto 4 decimal places from 1.5 to 2.5
def GenerateRandomValuesUptoFourDecimalP():
    import random
    randomlist = []
    for i in range(0,11):
        n = random.uniform(1.5,2.5)
        n = round(n,4)
        randomlist.append(n)
    return randomlist
print(GenerateRandomValuesUptoFourDecimalP())
