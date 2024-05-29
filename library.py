import math, tkinter as tk

class Liste:
    """This class allows you to create a list to which you can apply a multitude of sorting and search 
    algorithms. You are free to add your own algorithms or correct those that are implemented."""
    def __init__(self,liste):
        self.__liste = liste
        self.__length = len(liste)
        self.__binary_search_checks = 0

    def __str__(self):
        return "You can apply various sorting and search algorithms for lists."
    
    def get(self):
        return self.__liste
    
    def getLength(self):
        return self.__length
    
    def getBinarySearchChecks(self):
        return self.__binary_search_checks
    
    def set(self,liste):
        self.__liste = liste
        self.__length = len(liste)

    def printIt(self):
        print(self.__liste)
    
    #Algorithmes de tri
    def selection_sort(self):
        sorted_list_last_index = 0
        while sorted_list_last_index < self.__length-1:
            min_value_index = sorted_list_last_index
            for i in range(sorted_list_last_index+1,self.__length):
                if self.__liste[i] < self.__liste[min_value_index]:
                    min_value_index = i
            self.__liste[sorted_list_last_index], self.__liste[min_value_index] = self.__liste[min_value_index], self.__liste[sorted_list_last_index]
            sorted_list_last_index += 1

    def bubble_sort(self):
        sorted_list_first_index = self.__length-1
        while sorted_list_first_index > 0:
            for i in range(sorted_list_first_index):
                if self.__liste[i] > self.__liste[i+1]:
                    self.__liste[i], self.__liste[i+1] = self.__liste[i+1], self.__liste[i]
            sorted_list_first_index -= 1

    def insertion_sort(self):
        sorted_list_last_index = 0
        for i in range(sorted_list_last_index+1,self.__length):
            if self.__liste[i] < self.__liste[sorted_list_last_index]:
                saved_value = self.__liste[i]
                for j in range(sorted_list_last_index+1):
                    if self.__liste[i] < self.__liste[j]:
                        for k in range(i,j,-1):
                            self.__liste[k] = self.__liste[k-1]
                        self.__liste[j] = saved_value
                        break
            sorted_list_last_index += 1

    def __merge_sort_list_fusion(self,left_list, right_list):
        n,m = len(left_list),len(right_list)
        fusionned_list = list()
        while len(left_list) > 0 and len(right_list) > 0:
            if left_list[0] >= right_list[0]:
                fusionned_list.append(right_list[0])
                right_list.pop(0)
            else:
                fusionned_list.append(left_list[0])
                left_list.pop(0)
        if len(left_list) > 0:
            fusionned_list.extend(left_list)
        elif len(right_list) > 0:
            fusionned_list.extend(right_list)        
        return fusionned_list
    
    def divide_list(self,liste):
        n = len(liste)
        mid = n // 2
        left_list = liste[:mid]
        right_list = liste[mid:]
        return left_list, right_list
    
    def __merge_sort_algorithm(self,left_list, right_list):
        n,m = len(left_list),len(right_list)
        if n == 1 or m == 1:
            if n > 1:
                if left_list[0] > left_list[1]:
                    left_list.reverse()
            if m > 1:
                if right_list[0] > right_list[1]:
                    right_list.reverse()
            fusionned_list = self.__merge_sort_list_fusion(left_list, right_list)
            return fusionned_list
        else:
            left_left_list, left_right_list = self.divide_list(left_list)
            left_fusionned_list = self.__merge_sort_algorithm(left_left_list, left_right_list)
            right_left_list, right_right_list = self.divide_list(right_list)
            right_fusionned_list = self.__merge_sort_algorithm(right_left_list, right_right_list)
            fusionned_list = self.__merge_sort_list_fusion(left_fusionned_list, right_fusionned_list)
            return fusionned_list
        
    def merge_sort(self):
        left_list, right_list = self.divide_list(self.__liste)
        fusionned_list = self.__merge_sort_algorithm(left_list, right_list)
        self.__liste = fusionned_list

    #Algorithmes de recherche
    def linear_search(self,value):
        for i in range(self.__length):
            if self.__liste[i] == value:
                return i
        return None
    
    def __binary_search_algorithm(self,liste,value):
        n = len(liste)
        mid = n // 2
        if n == 1:
            if liste[0] == value:
                return 0
            else:
                self.__binary_search_checks += 1
                return -math.inf
        else:
            left_list = liste[:mid]
            right_list = liste[mid:]
            if value == liste[mid]:
                return mid
            elif value < liste[mid]:
                self.__binary_search_checks += 1
                return self.__binary_search_algorithm(left_list,value)
            else:
                self.__binary_search_checks += 1
                return mid + self.__binary_search_algorithm(right_list,value)
        
    def binary_search(self,value):
        return self.__binary_search_algorithm(self.__liste,value)


class Number_Guessing_Game:
    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.title("Number Guessing")
        self.number_guessed = tk.IntVar()
        self.entry = tk.Entry(self.fenetre,disabledbackground="white",disabledforeground="black",textvariable=self.number_guessed,state=tk.DISABLED)
        self.attempts_number = tk.IntVar()
        self.attempts = tk.Entry(self.fenetre,disabledbackground="white",disabledforeground="black",textvariable=self.attempts_number,state=tk.DISABLED)
        self.min_number = tk.IntVar()
        self.min = tk.Entry(self.fenetre,disabledbackground="white",disabledforeground="black",textvariable=self.min_number)
        self.max_number = tk.IntVar()
        self.max = tk.Entry(self.fenetre,disabledbackground="white",disabledforeground="black",textvariable=self.max_number)
        self.message = "Guessing the integer you imagine between min and max !"
        self.label_text = tk.StringVar()
        self.label_text.set(self.message)
        self.attempts_text = tk.StringVar()
        self.attempts_text.set("Attempts")
        self.min_text = tk.StringVar()
        self.min_text.set("Min")
        self.max_text = tk.StringVar()
        self.max_text.set("Max")
        self.value_text = tk.StringVar()
        self.value_text.set("Value")
        self.value_label = tk.Label(self.fenetre,textvariable=self.value_text)
        self.min_label = tk.Label(self.fenetre,textvariable=self.min_text)
        self.max_label = tk.Label(self.fenetre,textvariable=self.max_text)
        self.label = tk.Label(self.fenetre,textvariable=self.label_text)
        self.attempts_label = tk.Label(self.fenetre,textvariable=self.attempts_text)
        self.begin_button = tk.Button(self.fenetre,text="Begin",command=self.guess_number)
        self.lower_button = tk.Button(self.fenetre,text="Lower !",command=self.lower_search,state=tk.DISABLED)
        self.higher_button = tk.Button(self.fenetre,text="Higher !",command=self.higher_search,state=tk.DISABLED)
        self.reset_button = tk.Button(self.fenetre,text="Reset",command=self.reset_game,state=tk.DISABLED)
        self.quit_button = tk.Button(self.fenetre,text="Quit",command=self.fenetre.destroy)
        self.label.grid(row=0,column=0,columnspan=4,sticky=tk.W+tk.E)
        self.min_label.grid(row=1,column=0,columnspan=2,sticky=tk.W+tk.E)
        self.max_label.grid(row=1,column=2,columnspan=2,sticky=tk.W+tk.E)
        self.min.grid(row=2,column=0,columnspan=2,sticky=tk.W+tk.E)
        self.max.grid(row=2,column=2,columnspan=2,sticky=tk.W+tk.E)
        self.value_label.grid(row=3,column=0,columnspan=2,sticky=tk.W+tk.E)
        self.attempts_label.grid(row=3,column=2,columnspan=2,sticky=tk.W+tk.E)
        self.entry.grid(row=4,column=0,columnspan=2,sticky=tk.W+tk.E)
        self.attempts.grid(row=4,column=2,sticky=tk.W+tk.E)
        self.begin_button.grid(row=5,column=0)
        self.lower_button.grid(row=5,column=1)
        self.higher_button.grid(row=5,column=2)
        self.reset_button.grid(row=6,column=0)
        self.quit_button.grid(row=6,column=2)
        self.fenetre.mainloop()

    def check_min_max(self):
        if self.min_value > self.max_value or self.min_value < 0 or self.max_value < 0:
            return False
        else:
            return True
    
    def guess_number(self):
        problem = 0
        try:
            self.min_value,self.max_value = self.min_number.get(),self.max_number.get()
        except Exception as e:
            self.reset_game
            problem = 1
        if problem == 0:
            if not(self.check_min_max()):
                self.reset_game
            else:
                self.numbers_range = Liste([i for i in range(self.min_value,self.max_value+1)])
                self.min.config(state=tk.DISABLED)
                self.max.config(state=tk.DISABLED)
                self.lower_button.config(state=tk.NORMAL)
                self.higher_button.config(state=tk.NORMAL)
                self.reset_button.config(state=tk.NORMAL)
                self.begin_button.config(state=tk.DISABLED)
                liste = self.numbers_range.get()
                list_length = self.numbers_range.getLength()
                mid = (list_length // 2)
                self.number_guessed.set(liste[mid])
                self.attempts_number.set(self.attempts_number.get() + 1)

    def lower_search(self):
        if self.numbers_range.getLength() == 1:
            self.label_text.set("Can't go lower !")
            self.lower_button.config(state=tk.DISABLED)
            self.higher_button.config(state=tk.DISABLED)
        else:
            left_list,right_list = self.numbers_range.divide_list(self.numbers_range.get())
            self.numbers_range.set(left_list)
            liste = self.numbers_range.get()
            list_length = self.numbers_range.getLength()
            mid = (list_length // 2)
            self.number_guessed.set(liste[mid])
            self.attempts_number.set(self.attempts_number.get() + 1)

    def higher_search(self):
        if self.numbers_range.getLength() == 1:
            self.label_text.set("Can't go higher !")
            self.lower_button.config(state=tk.DISABLED)
            self.higher_button.config(state=tk.DISABLED)
        else:
            left_list,right_list = self.numbers_range.divide_list(self.numbers_range.get())
            self.numbers_range.set(right_list)
            liste = self.numbers_range.get()
            list_length = self.numbers_range.getLength()
            mid = (list_length // 2)
            self.number_guessed.set(liste[mid])
            self.attempts_number.set(self.attempts_number.get() + 1)

    def reset_game(self):
        self.min.config(state=tk.NORMAL)
        self.max.config(state=tk.NORMAL)
        self.min_number.set(0)
        self.max_number.set(0)
        self.lower_button.config(state=tk.DISABLED)
        self.higher_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.DISABLED)
        self.begin_button.config(state=tk.NORMAL)
        self.number_guessed.set(0)
        self.attempts_number.set(0)
        self.numbers_range.set([i for i in range(self.min_value,self.max_value+1)])
        self.label_text.set(self.message)


