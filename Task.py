
#TEST-1

#Q.1 write a program for Ascending and Descending order without using the inbuilt method.?


def asc_lst(lst):
    for i in range(len(lst) - 1):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

def dsc_lst(lst):
    for i in range(len(lst) - 1):
        max_idx = i
        for j in range(i + 1, len(lst)):
            if lst[j] > lst[max_idx]:
                max_idx = j
        lst[i], lst[max_idx] = lst[max_idx], lst[i]
    return lst

lst = [3,5,2,4,6,7,3]
print(asc_lst(lst))
print(dsc_lst(lst))

#2.Find the largest number in a given List without using the inbuilt method?

lst = [20,25,10,45,22,50,40]
large = 0
for i in lst:
    if large<i:
        large=i
print(large)

#3.Write a program for single inheritance in python?

class Student:
    def test(self):
        print("Take quiz")

class Teacher(Student):
    def quiz(self):
        print("Give quiz in test")

teacher = Teacher()
teacher.test()
teacher.quiz()

#4.Write a program for overloading and overriding.

#overloading
class Math:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c
    
    def multiply(self, a, b, c):
        return a*b*c
    
cal = Math()
print(cal.multiply(5,6,5))

#overriding
class Student:
    def test(self):
        print("Take quiz")

class Teacher(Student):
    def quiz(self):
        print("Give quiz in test")

student = Student()
student.test()

teacher = Teacher()
teacher.quiz()

#6.Write a program to add two matrices.

X= [[1,2,3],[4,5,6],[7,8,9]]

Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]

added_mat = []
for i in range(len(X)):
    row = []
    for j in range(len(X[0])):
        row.append(X[i][j]+Y[i][j])
    added_mat.append(row)
print(added_mat)


#TEST-2

#3. Create a voice recorder using python.

import sounddevice as sd
import wave

def record_voice(filename):
    """Records voice and saves it to a file."""

    # Record audio for 10 seconds
    duration = 10
    samplerate = 44100
    frames = int(duration * samplerate)
    
    recording = sd.rec(frames=frames, samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()

    # Save the recorded audio to a file
    with wave.open(filename, 'wb') as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(samplerate)
        f.writeframes(recording.tobytes())

if __name__ == '__main__':
    # Give filename as you want 
    filename = input('Enter the filename to save the recording to: ')

    # Record the voice
    record_voice(filename)

    # Print a message to the user
    print('Recording saved to {}'.format(filename))
