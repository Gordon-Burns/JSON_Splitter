import json

num_splits = 4
# Read the input JSON file
with open("Big_JSON.json", 'r') as fileread:
  jsoncontent = json.load(fileread)

  # Calculate the size of each split
  total_length = len(jsoncontent)
  split_size = total_length // num_splits
  remainder = total_length % num_splits

  start = 0
  for i in range(num_splits):
      # Determine the end index for the current split
      end = start + split_size + (1 if i < remainder else 0)  # Distribute remainder among the first few splits
      split_content = jsoncontent[start:end]

    # Write the split content to a new file
      output_file = f"file_{i+1}.json"
      with open(output_file, 'w') as json_file:
          json.dump(split_content, json_file)

          start = end

  print(f"Files have been successfully split into {num_splits} parts.")