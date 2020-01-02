import json
import os
import hashlib

def get_hash(filename):
    blockchain_dir=os.curdir+'/chain/'
    file = open(blockchain_dir+filename, 'rb').read() #режим чтения бинарных данных
    return hashlib.md5(file).hexdigest()


def write_block(name, amount, to_whom, prev_hash=''):
	
    blockchain_dir=os.curdir+'/chain/' # blockchaindirectory
    files=os.listdir(blockchain_dir)   # список строк из имен блоков
    files=sorted([int(i) for i in files]) #сортируем список блоков
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
