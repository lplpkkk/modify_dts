import re




def check_variable(value, threshold):
    assert value <= threshold, f'變數的值 {value} 超過了閾值 {threshold}'
    



def find_macro_value(path_to_h, parameter_name):
    with open(path_to_h, 'r') as file:
        content = file.read()

    # 使用正則表達式搜尋參數對應的macro
    pattern = r'#define\s+' + parameter_name + r'\s+(\S+)'
    match = re.search(pattern, content)

    if match:
        macro_value = match.group(1)
        print(f'{parameter_name}的macro值為{macro_value}。')
        return macro_value
    else:
        print(f'找不到{parameter_name}的macro。')
        return None

# 指定.h檔案路徑和參數名稱
path_to_h = '//Users/yangzikuan/Desktop/optee_size.h'
parameter_name = 'OPTEE_SIZE'
parameter_name_max_size = 'OPTEE_SIZE_MAX'

# 呼叫函式尋找對應的macro值
macro_value = find_macro_value(path_to_h, parameter_name)
max_size = find_macro_value(path_to_h, parameter_name_max_size)

check_variable(macro_value,max_size)


def modify_dtsi_reg_property(path_to_dtsi, node_name, new_reg_value):
    with open(path_to_dtsi, 'r') as file:
        content = file.read()

    # 使用正則表達式搜尋指定的device tree node及其reg屬性
    pattern = r'(\s*' + node_name + r'\s*{\s*[\S\s]*?reg\s*=\s*<)(.*?)>([\S\s]*?};)'
    match = re.search(pattern, content)

    if match:
        original_reg_property = match.group(2)
        modified_reg_property = f'{new_reg_value}'

        # 將reg屬性替換為新的值
        modified_content = content.replace(original_reg_property, modified_reg_property)

        # 將修改後的內容寫回檔案
        with open(path_to_dtsi, 'w') as file:
            file.write(modified_content)

        print(f'{node_name}的reg屬性已成功修改為{new_reg_value}。')
    else:
        print(f'找不到指定的device tree node：{node_name}。')

# 指定dtsi檔案路徑、device tree node名稱和新的reg值
path_to_dtsi = '//Users/yangzikuan/Desktop/test.dtsi'
node_name = 'spi@f0004000'
new_reg_value = '0xdeadbeef '+ macro_value



# 呼叫函式進行修改
modify_dtsi_reg_property(path_to_dtsi, node_name, new_reg_value)


# modify_dtsi_file(path_to_dtsi, new_reg_value)
