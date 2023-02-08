
import glob
import sys

def main():
  '''main method'''
  input_path = '/home/data'
  output_path = '/home/output/result.txt'
  # input_path = './data'
  # output_path = './result.txt'

  file_names = []
  for file in glob.glob(f'{input_path}/*.txt'):
    file_names.append(file)
  
  # print('\n'.join(file_names))
  with open(output_path, 'w+') as file_handler:
    file_handler.write('#'*50)
    file_handler.write('\n')
    file_handler.write('FILE NAMES:\n')
    file_handler.write('\n'.join(file_names))
    file_handler.write('\n')
    file_handler.write('#'*50)
    file_handler.write('\n')
  
  with open(output_path) as file_handler:
    lines = file_handler.readlines()
    print(''.join(lines))


if __name__=='__main__':
  main()