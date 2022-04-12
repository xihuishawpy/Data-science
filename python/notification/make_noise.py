import os 

def make_noise():
    '''Make noise after finishing executing a code'''
    os.system('play -nq -t alsa synth 1 sine 440')

def main():
    even_arr = [i for i in range(10000) if i%2==0]
    make_noise()

if __name__=='__main__':
    main()