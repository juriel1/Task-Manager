class Data_manager():
    def __init__(self):
        self.task_dict = dict()  
        self.count_task = int()

    def set_new_task(self,data_content:str,status:str):
        self.count_task += 1
        print(self.count_task)
        self.task_dict[data_content] = status+"$"+str(self.count_task)

    def set_task(self,data_content:str,status:str):
        count = self.task_dict[data_content][-1]
        self.task_dict[data_content] = status +"$"+str(count)

    def change_task(self,data_content:str,new_data_content:str):
        self.task_dict[new_data_content] = self.task_dict.pop(data_content)

    def remove_task(self,data_content:str):
        self.count_task -=1
        del self.task_dict[data_content]

    def save_data(self):
        with open('Soucource/data/fs.txt', 'w') as f:            
            for i in self.task_dict.keys():
                f.write(i+"$"+self.task_dict[i]+"\n")
                print("Task: {} -- Status: {}".format(i,self.task_dict[i]))
        print("write file save")

    #def load():