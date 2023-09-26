import json
class jsonconfig():
  def read(self, filepath):
    print("Reading jsondata..")
    with open(filepath, 'r') as file:
        date = json.load(file)
    return date

  def write(self, date, filepath): 
      print("Writing config to jsondata..")
      with open(filepath, 'w') as file:
          json.dump(date, file, indent=4)  # indent=4でフォーマットを整形して書き込み
      return date