
import glob
import os
import socket

def main():
  '''Main method'''
  input_path = '/home/data'
  output_path = '/home/output/result.txt'

  file_info = {}
  for file_path in glob.glob(f'{input_path}/*.txt'):
    file_name = os.path.basename(file_path)
    content = _get_file_content(file_path)

    word_count = _get_word_count(content)
    word_frequencies = _get_word_frequencies(content)
    top_3_frequencies = _get_top_by_frequencies(limit=3, frequencies=word_frequencies)
    
    file_info[file_name] = {
      'frequencies': word_frequencies,
      'name': file_name,
      'path': file_path,
      'top_3_frequencies': top_3_frequencies,
      'total_count': word_count,
    }

  with open(output_path, 'w+') as file_handler:
    ip_address = _get_ip_address()
    total_word_count = 0
    
    file_names = ', '.join([value.get('name') for value in file_info.values()])
    file_handler.write(f'\nFiles: {file_names}\n\n')

    for info in file_info.values():
      word_count = info.get('total_count')
      total_word_count += word_count
      file_handler.write(f'File info of {info.get("name")}:\n')
      file_handler.write(f'Total word count: {word_count}\n')
      file_handler.write(f'Top 3 words by frequencies: {info.get("top_3_frequencies")}\n\n')
    
    file_handler.write(f'Combined word count: {total_word_count}\n\n')

    file_handler.write(f'IP Address: {ip_address}\n')

  _print_from_output(output_path)

def _get_file_content(file_path=None):
  '''Read file content'''
  content = None
  with open(file_path, 'r', encoding='UTF-8') as file_handler:
    content = file_handler.read()
  return content

def _get_ip_address():
  '''Get machine ip address'''
  host_name = socket.gethostname()
  return socket.gethostbyname(host_name)

def _get_top_by_frequencies(limit=0, frequencies={}):
  '''Get top K words based on frequencies'''
  limit = min(limit, len(frequencies))
  sorted_by_freq = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)
  return sorted_by_freq[:limit]

def _get_word_count(content):
  '''Count total number of words'''
  count = 0
  if content:
    count = len(content.split())
  return count

def _get_word_frequencies(content):
  '''Get word frequencies of a given file'''
  frequencies = {}
  if content:
    words = content.split()
    word_freq = [words.count(word) for word in words]
    frequencies = dict(zip(words,word_freq))
  return frequencies

def _print_from_output(file_path):
  '''Print output file content'''
  with open(file_path, 'r') as file_handler:
    lines = file_handler.readlines()
    print(''.join(lines))


if __name__=='__main__':
  main()