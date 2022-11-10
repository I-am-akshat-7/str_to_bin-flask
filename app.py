from flask import Flask,redirect,url_for,render_template,request
import binascii
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        
        # Handle POST Request here
        try:
            
            if type(int(request.form['x'])) == int:
                print('yes')
        except: 
            
            print('no')
            
        
        return render_template('index.html', k=str_to_bin(request.form['x']))
    return render_template('index.html', k='')

def str_to_bin(n):
    try:
        
        n2 = int(n,2)
        n3 = n2.to_bytes((n2.bit_length() + 7) // 8, 'big').decode()
    
    
        return n3
    except:
        res = ''.join(format(ord(i), '08b') for i in n)
        return res
        
    
    
if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)