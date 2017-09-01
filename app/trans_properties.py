import os
import xlrd
from config import basedir


class TransProperties(object):
    def __init__(self, package, excel):
        self.package = package
        self.excel = excel
        self.tmp_properties = basedir + '/files/temp/tmp.properties'
        self.dictory_properties = self.read_package()
        self.dictory_excel = self.read_excel()

    @staticmethod
    def array_to_dictory(array_1, array_2):
        '''
        :param array_1: keys
        :param array_2: values
        :return: dictory
        '''
        dictory = {}
        for i in range(len(array_1)):
            dictory[array_1[i]] = array_2[i]
        return dictory

    def read_package(self):
        variables, languages = [], []
        with open(self.package, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                a, b = line.split(' = ')[0], line.split(' = ')[-1]
                variables.append(a.strip('\n').strip(' ').strip('\t'))
                languages.append(b.strip('\n').strip(' ').strip('\t'))
            print('Read {0} successfully!'.format(self.package))
            return self.array_to_dictory(variables, languages)

    def read_excel(self):
        workbook = xlrd.open_workbook(self.excel, encoding_override='utf-8')
        sheet = workbook.sheet_by_index(0)
        variables, language = [], []
        for i in range(1, len(sheet.col(0))):
            variables.append(sheet.col(0)[i].value)
            language.append(sheet.col(2)[i].value)
        print('Read {0} successfully!'.format(self.excel))
        return self.array_to_dictory(variables, language)

    @staticmethod
    def combine(dictory_properties, dictory_excel):
        '''
        :param dictory_properties: original dictory
        :param dictory_excel: new keys and values
        :return: original dictory add new dictory
        '''
        print(dictory_properties, dictory_excel)
        for key in dictory_excel:
            dictory_properties[key] = dictory_excel[key]
        return dictory_properties

    @staticmethod
    def write_package(dictory, filename):
        '''
        :param dictory: dictory contains properties' variables
        :param filename: properties file
        :return: None
        '''
        with open(filename, 'w', encoding='utf-8') as f:
            for key in dictory:
                if key == dictory[key]:
                    string = '{0}\n'.format(key)
                else:
                    string = '{0} = {1}\n'.format(key, dictory[key])
                f.write(string)

    @staticmethod
    def code_reverse(input_file, output_file, type):
        '''
        :param input_file: file to be transfer code;
        :param output_file: file to store the output;
        :param type: 1 to unicode; 0 to ascii;
        :return: None;
        '''
        if type == 1:
            command = 'native2ascii -reverse -encoding utf-8 ./' + input_file + ' ./' + output_file
            os.system(command=command)
        elif type == 0:
            command = 'native2ascii -encoding utf-8 ./' + input_file + ' ./' + output_file
            os.system(command=command)
        else:
            raise TypeError('I have no idea about this transference.')

    def transfer(self):
        self.code_reverse(self.package, self.tmp_properties, 1)
        self.write_package(self.combine(self.dictory_properties, self.dictory_excel), self.tmp_properties)
        self.code_reverse('tmp.properties', 'output.properties', 0)

if __name__ == '__main__':
    example = TransProperties('package.properties', 'translate.xlsx')
    example.transfer()
