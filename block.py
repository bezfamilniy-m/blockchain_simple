import json
import os
import hashlib

blockchain_dir=os.curdir+'/chain/' # blockchaindirectory

def get_files():
    files=os.listdir(blockchain_dir)   # список строк из имен блоков    
    return sorted([init(i) for i in files])

def get_hash(filename):
    file = open(blockchain_dir+filename, 'rb').read() #режим чтения бинарных данных
    return hashlib.md5(file).hexdigest()

def check_integrity():
    #1 сичтать хэш предыдущего блока
    #2 вычислить хэш предыдущего блока
    #3 сравнить полученные данные
    files=get_files()
    files=sorted([int(i) for i in files]) #сортируем список блоков 
    for file in files[1:]:
        h=json.load(open(blockchain_dir+str(file)))['hash']
        actual_hash=get_hash(srt(file-1)) #получение номера предыдущего блока с приведением к типу string! так как нельзя забывать о типе
        if h==actual_hash:
            res='ok'
        else:
            res='corrupted'
    print('block {} is {}'.format(str(file-1),res)
    
def write_block(name,amount,to_whom):
    files=get_files()
    last_file=files[-1] #взять номер посленднего блока
    file_name=str(last_file+1) #инкремент имени последнего блока
    prev_hash=get_hash(str(last_file))
    data={ 'name': name,
           'amount': amount,
           'to_whom': to_whom,
           'hash': prev_hash}
    with open(blockchain_dir+file_name, 'w') as file:
        json.dump(data,file, indent=4, ensure_ascii=False)

def main():
    write_block(name='ivan',amount=4, to_whom='kate')

if __name__=='__main__':
	main()
