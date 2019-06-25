# assignement 3
from tkinter import *

import time
import textwrap

from tkinter import messagebox
from tkinter import simpledialog
import random
from tkinter import ttk

#perment list to store student information
STUDENT_LIST_QUICK = []
STUDENT_LIST_LONG = []

# temporary list
STUDENT_LIST_TEMP_QUICK = []
STUDENT_LIST_TEMP_LONG = []

# list to store time difference of joinig the queue
LABEL_LIST_TIME_QUICK = []
LABEL_LIST_TIME_LONG = []

# permanent dictionary to store students information
STUDENT_DICT_QUICK = {}
STUDENT_DICT_LONG = {}

#temporary dictionary
STUDENT_DICT_TEMP_QUICK = {}
STUDENT_DICT_TEMP_LONG = {}





class ControlUniPrime(Frame):
    """A control class containing widgets which display the queue information and the student average wait time"""

    def __init__(self,master):

        """Constructs the display window which accommodates the topmost widgets .
        Parameters:
            master (tk.Tk|tk.Frame): The frame widget.

        """

        super().__init__(master)
        self._master = master
        self._frame_welcome_messg = Frame(self._master, bg='#fefbed' )
        self._frame_welcome_messg.pack(fill= X)

        self._welcome_messg = Label(self._frame_welcome_messg, text = '\nImportant:',fg='#C09853', bg ='#fefbed', font ='arial 18 bold')
        self._welcome_messg.pack(padx=15,anchor = W,expand = True)

        self._welcome_messg = Label(self._frame_welcome_messg, text = 'Individual assessment items must be solely your own work.While students are encouraged to have high-level conversations about the problems they are trying to solve, you must not look at another student\'s code or copy from it. The University uses sophisticated anti-collusion measures to automatically detect similarity between assignment submission.\n', fg='#333',bg='#fefbed',wraplength=1000,justify=LEFT)
        self._welcome_messg.pack(side =LEFT,anchor=W,padx=15,fill = BOTH)



        self._questions_frame=Frame(self._master)
        self._questions_frame.pack(pady = 5,fill=X)




        self._frame_question_quick= Frame(self._questions_frame, bg = '#dff0d8',highlightbackground = '#d6e9c6',highlightthickness=2)
        self._frame_question_quick.pack(side = LEFT,expand=True, padx = 15,pady = 5,fill = X)

        self._quick_quest = Label(self._frame_question_quick, text = 'Quick Questions', fg='#3c763d',bg = '#dff0d8',font = 'arial 30 bold')
        self._quick_quest.pack(ipady = 10)

        self._time_tutor = Label(self._frame_question_quick, text = '< 2 mins with a tutor', fg = '#666', bg = '#dff0d8',font = 'none 21 italic')
        self._time_tutor.pack(side = TOP, ipady = 10)



        self._frame_question_long= Frame(self._questions_frame,bg = '#d9edf7',highlightbackground = '#bce8f1',highlightthickness=2)
        self._frame_question_long.pack(side = LEFT,expand=True, padx = 15,fill = X)

        self._long_quest = Label(self._frame_question_long, text = 'Long Questions', fg='#31708f',bg = '#d9edf7',font = 'arial 30 bold')
        self._long_quest.pack(ipady = 10)

        self._time_tutor_long = Label(self._frame_question_long, text = '> 2 mins with a tutor', fg = '#666', bg = '#d9edf7',font = 'none 21 italic')
        self._time_tutor_long.pack(side = TOP, ipady = 10)


        self._frame_example=Frame(self._master)
        separator_query = ttk.Separator(self.master, orient='horizontal')
        self._frame_example.pack(fill=X)
        separator_query.pack(fill=X)


        self._frame_question_exampl_quick= Frame(self._frame_example)
        self._frame_question_exampl_quick.pack(side = LEFT,expand=True, padx = 15,pady = 5,fill = X)


        self._example_quick = Label(self._frame_question_exampl_quick,text='Some examples of quick questions:', font = 14)#
        self._example_quick.pack(anchor=W,pady=5)

        self._example_quick = Label(self._frame_question_exampl_quick,text=u'      \u2022Syntax errors', font = 14)#
        self._example_quick.pack(anchor=W,pady=0)
        self._example_quick = Label(self._frame_question_exampl_quick,text=u'      \u2022Interpreting error output', font = 14)#
        self._example_quick.pack(anchor=W)
        self._example_quick = Label(self._frame_question_exampl_quick,text=u'      \u2022Assignment/MyPytutor interpretation', font = 14)#
        self._example_quick.pack(anchor=W)
        self._example_quick = Label(self._frame_question_exampl_quick,text=u'      \u2022MyPytutor submission issues\n', font = 14)#
        self._example_quick.pack(anchor=W)

## Right side information of the the application => the long help request


        self._frame_question_exampl_long= Frame(self._frame_example)
        self._frame_question_exampl_long.pack(side = LEFT,expand=True, padx = 15,pady = 5,fill = X)


        self._example_long = Label(self._frame_question_exampl_long, text='Some examples of long questions:', font = 14)
        self._example_long.pack(anchor=W, pady = 5)

        self._example_long = Label(self._frame_question_exampl_long, text=u'    \u2022Open ended question', font = 14)
        self._example_long.pack(anchor=W)
        self._example_long = Label(self._frame_question_exampl_long, text=u'    \u2022How to start a problem', font = 14)
        self._example_long.pack(anchor=W)
        self._example_long = Label(self._frame_question_exampl_long, text=u'    \u2022how to improve code', font = 14)
        self._example_long.pack(anchor=W)
        self._example_long = Label(self._frame_question_exampl_long, text=u'    \u2022Debugging', font = 14)
        self._example_long.pack(anchor=W)
        self._example_long = Label(self._frame_question_exampl_long, text=u'    \u2022Assignment help\n', font = 14)
        self._example_long.pack(anchor=W)



        button_request_short =Button(self._frame_question_exampl_quick, text='Request Quick Help',font = 'arial 14 bold',fg = '#fff', bg ='#5cb85c',width =len('Request Quick Help'),height = 2, highlightbackground = '#4cae4c',highlightthickness=2,command = self.click_short)
        button_request_short.pack(anchor=CENTER)

        button_request_long =Button(self._frame_question_exampl_long, text='Request Long Help',font = 'arial 14 bold',fg = '#fff', bg ='#46b8da',width =len('Request Long Help'),height = 2, highlightbackground = '#5bc0de',highlightthickness=2,command = self.click_long)
        button_request_long.pack(anchor=CENTER)



        self._frame_student = Frame(self._master,highlightbackground = 'grey93',highlightthickness=2)
        separator_1 = ttk.Separator(self.master, orient='horizontal')
        self._frame_name_time = Frame(self._master, highlightbackground='grey93', highlightthickness=2)
        separator_2 = ttk.Separator(self.master, orient='horizontal')

        self._frame_student.pack(fill=X)
        separator_1.pack(fill=X)
        self._frame_name_time.pack(fill=X)
        separator_2.pack(fill=X)



        self._frame_student_quick=Frame(self._frame_student)
        self._frame_student_quick.pack(side = LEFT,expand=True, padx = 15,pady = 5,fill = X)

        self._no_students_quick=Label(self._frame_student_quick, text = 'No student in queue', font = 14)
        self._no_students_quick.pack(side=LEFT, padx = 5, pady = 3,fill = X)


        self._frame_student_long=Frame(self._frame_student)
        self._frame_student_long.pack(side = LEFT,expand=True, padx = 10,pady = 5,fill = X)

        self._no_students_long=Label(self._frame_student_long, text = 'No student in queue', font = 14)
        self._no_students_long.pack(side=LEFT, padx = 10,pady = 3,fill = X)


        self._frame_name_time_quick=Frame(self._frame_name_time)
        self._frame_name_time_quick.pack(side = LEFT,expand=True, padx = 15,pady = 10,fill = X)

        self._frame_label_name_time_quick = Label(self._frame_name_time_quick,text='#', font = ('arial 14 bold'))
        self._frame_label_name_time_quick.pack(side=LEFT)
        self._frame_label_name_time_quick = Label(self._frame_name_time_quick,text='Name', font = ('arial 14 bold'))
        self._frame_label_name_time_quick.pack(side=LEFT, padx =10)
        self._frame_label_name_time_quick = Label(self._frame_name_time_quick,text='Questions Today ?', font = ('arial 14 bold'))
        self._frame_label_name_time_quick.pack(side=LEFT, expand = True, fill = X)
        self._frame_label_name_time_quick = Label(self._frame_name_time_quick,text='Time', font = ('arial 14 bold'))
        self._frame_label_name_time_quick.pack(side=LEFT,padx = 15)

        self._frame_label_name_time_quick = Label(self._frame_name_time_quick,text='      ', font = ('arial 14 bold'))
        self._frame_label_name_time_quick.pack(side=LEFT)


        self._frame_name_time_long=Frame(self._frame_name_time)
        self._frame_name_time_long.pack(side = LEFT,expand=True, padx = 15,pady = 10,fill = X)

        ## Long help request widgets
        self._frame_label_name_time_long = Label(self._frame_name_time_long,text='  #', font = ('arial 14 bold'))
        self._frame_label_name_time_long.pack(side=LEFT)
        self._frame_label_name_time_long = Label(self._frame_name_time_long,text='Name', font = ('arial 14 bold'))
        self._frame_label_name_time_long.pack(side=LEFT, padx = 10)
        self._frame_label_name_time_long = Label(self._frame_name_time_long,text='Questions Today ?', font = ('arial 14 bold'))
        self._frame_label_name_time_long.pack(side=LEFT, expand = True, fill = X)
        self._frame_label_name_time_long = Label(self._frame_name_time_long,text='Time', font = ('arial 14 bold'))
        self._frame_label_name_time_long.pack(side=LEFT,padx=15)

        self._frame_label_name_time_long = Label(self._frame_name_time_long,text='      ', font = ('arial 14 bold'))
        self._frame_label_name_time_long.pack(side=LEFT)

        # Packing the second control class so that it methods are accessed
        self.control_uni = ContolUniSeco(master)
        self.control_uni.pack(expand = True,fill=X)

    def click_short(self):
        """A method that enable the students to join the quick help queue"""

        self.control_uni.validation_quick()

    def click_long(self):
        """A method that enable the students to join the long help queue"""

        self.control_uni.validation_long()

    def change_label_quick(self):
        """
        Change the label after of the student join the quick help queue.
        Iff there are students on the queue, an average wait time is displayed otherwise "No student in queue is displayed".
        """

        if len(STUDENT_LIST_TEMP_QUICK) > 0:

            student_number = len(STUDENT_LIST_TEMP_QUICK)
            total_time_on_queue = sum(LABEL_LIST_TIME_QUICK)
            mean_wait_time = total_time_on_queue//student_number

            if mean_wait_time < 60:
                self._no_students_quick.config(text=f'An average wait time of few seconds for {student_number} students',font = ('none 14 italic'))


            elif mean_wait_time < 120:
                self._no_students_quick.config(text=f'An average wait time of about a minute for {student_number} students',font = ('none 14 italic'))

            elif mean_wait_time  < 3600:
                timely = int(mean_wait_time//60)
                self._no_students_quick.config(text=f'An average wait time of {timely} minutes for {student_number} students',font = ('none 14 italic'))

            elif mean_wait_time < 7200:
                self._no_students_quick.config(text=f'An average wait time of about an hour for {student_number} students',font = ('none 14 italic'))

            elif mean_wait_time >= 7200:
                timely = int(mean_wait_time//3600)
                self._no_students_quick.config(text=f'An average wait time of {timely} hours for {student_number} students',font = ('none 14 italic'))
        else:
            self._no_students_quick.config(text = '        No student in queue')



    def change_label_long(self):
        """Change the label after of the student join the long help queue.
        Iff there are students on the queue, an average wait time is displayed otherwise "No student in queue is displayed".

        """

        if len(STUDENT_LIST_TEMP_LONG) > 0:

            student_number = len(STUDENT_LIST_TEMP_LONG)
            total_time_on_queue = sum(LABEL_LIST_TIME_LONG)
            mean_wait_time = total_time_on_queue//student_number

            if mean_wait_time < 60:
                self._no_students_long.config(text=f'An average wait time of few seconds for {student_number} students',font = ('none 14 italic'))

            elif mean_wait_time < 120:
                self._no_students_long.config(text=f'An average wait time of about a minute for {student_number} students',font = ('none 14 italic'))

            elif mean_wait_time  < 3600:
                timely = int(mean_wait_time//60)
                self._no_students_long.config(text=f'An average wait time of {timely} minutes for {student_number} students',font = ('none 14 italic'))

            elif mean_wait_time < 7200:
                self._no_students_long.config(text=f'An average wait time of about an hour for {student_number} students',font = ('none 14 italic'))

            elif mean_wait_time >= 7200:
                timely = int(mean_wait_time//3600)
                self._no_students_long.config(text=f'An average wait time of {timely} hours for {student_number} students',font = ('none 14 italic'))

        else:
            self._no_students_long.config(text = '        No student in queue')
    def label_upadate(self):
        """A method which control average wait time label for both queue after 10 second"""

        self.change_label_long()
        self.change_label_quick()




class StudentEntry(Frame):
    """ A class which stores students information"""
    def __init__(self, parent, number, name, questions_asked,time_join, start_time):
        """Constructs student's class Frame to store information and keep track of the update
        Parameters:
            master (tk.Tk|tk.Frame): a frame where this class is packed .
            number (int): the number of student on the queue.
            name (str): The name of the student.
            question_asked(int): the number of question the student has asked since the opening of the application.
            time_join(int): The time in second the student has joined the queue.
            start_time(str): a text message to be used as label on the queue which display how long the student has waited on the queue.

        """

        super().__init__(parent)
        self._question_asked = questions_asked
        self.student_name = name
        self.start_time = start_time
        self._number = number
        self._time_join = time_join

        self._label_number = Label(self, text = f'{self._number}')
        self._label_number.pack(side = LEFT,padx =10)
        self._label_student = Label(self, text = name )
        self._label_student.pack(side=LEFT, padx = 10)
        self._label_question = Label(self, text = f'{(questions_asked)}' )
        self._label_question.pack(side=LEFT, padx = 15,expand = True, fill = X)
        self._label_time = Label(self, text = self.start_time )
        self._label_time.pack(side=LEFT)
        self._button_red = Button(self,  bg ='tomato',width = 1,height = 1,highlightbackground = 'red',highlightthickness=2,command = self.remove_student_red )  # changing the colour to red
        self._button_red.pack(side=LEFT)
        self._button_green = Button(self, bg ='#5cb85c',width = 1,height = 1,highlightbackground = '#4cae4c',highlightthickness=2, command = self.remove_student_green)
        self._button_green.pack(side=LEFT)

    def set_time(self,time_now):
        """Method which changes the student's join queue label after 10 seconds.
        Parameter:
            time_now(str): a text which desplays how long the student has been on the queue."""
        self.start_time = time_now
        # changing the time label widget after 10 second.
        self._label_time.config(text = self.start_time)

    def set_number(self, student_num):
        """Method which changes the student'a number on the queue after 10 seconds.
        Parameter:
            student_num(int): an number(int)  which shows the position of the student on the queue. """
        self._number = student_num
        self._label_number.config(text=f'{self._number}')

    def get_name(self):
        """Return the name of the student.
        Return:
            student_name(str): the name of the student associated with this class
        """
        return self.student_name

    def get_question(self):
        """Return the number of question has asked since the joined the queue.
        Return:
            _question_asked(int): question(int) number of question the student has asked since the opening of the app.
        """
        return self._question_asked

    def get_time(self):
        """Return the time this student has join the queue.
        Return:
            time_join(int): return the time this student has joined the queue.
        """
        return self._time_join


    def remove_student_red(self):
        """Method which remove the student from either queue when the red button is pressed"""

        # removing student on the quick queue
        if self.student_name in STUDENT_LIST_TEMP_QUICK:

            STUDENT_LIST_TEMP_QUICK.remove(self.student_name)
            del STUDENT_DICT_TEMP_QUICK[self.student_name]
            frame = STUDENT_DICT_QUICK[self.student_name][0]
            frame.destroy()

        else: # removing the student on the long queue

            STUDENT_LIST_TEMP_LONG.remove(self.student_name)
            del STUDENT_DICT_TEMP_LONG[self.student_name]
            frame = STUDENT_DICT_LONG[self.student_name][0]
            frame.destroy()




    def remove_student_green(self):
        """Method which remove the student from either queue when the green button is pressed"""
        if self.student_name in STUDENT_LIST_TEMP_QUICK: # removing the student on the quick queue


            STUDENT_LIST_QUICK.append(self.student_name)
            # adding this student is perment list to keep track of their questions asked
            STUDENT_LIST_TEMP_QUICK.remove(self.student_name)

            del STUDENT_DICT_TEMP_QUICK[self.student_name]
            frame = STUDENT_DICT_QUICK[self.student_name][0]
            frame.destroy()

        else: #for removing student in the long queue

            # adding this student is perment list to keep track of their questions asked
            STUDENT_LIST_LONG.append(self.student_name)

            STUDENT_LIST_TEMP_LONG.remove(self.student_name)
            del STUDENT_DICT_TEMP_LONG[self.student_name]
            frame = STUDENT_DICT_LONG[self.student_name][0]
            frame.destroy()

    def __str__(self):
        """Return the string associated with this student class"""

        if self.student_name in STUDENT_DICT_TEMP_QUICK:
            return STUDENT_DICT_TEMP_QUICK[self.student_name]

        return f'{self.student_name}:{STUDENT_DICT_TEMP_LONG[self.student_name]}'
    def __repr__(self):
        """Return the string associated with this student class"""
        return str(self)







class ContolUniSeco(Frame):
    """A secondary control class containing widgets and functionality of the queue."""

    def __init__(self, parent):

        """Constructs the display window which accommodates the topmost widgets .
        Parameters:
            parent (tk.Tk|tk.Frame): The frame widget window which accommodates other widgets and enable the functionality of the queue.

        """
        super().__init__(parent)
        self._texted_entry_quick = ''
        self._texted_entry_long = ''

        self._student_list_temp_quick = []
        self._student_list_temp_long = []


        self.is_valid_quick = True
        self.is_valid_long = True

        # frame of the student class
        self._frame_class = Frame(parent)
        self._frame_class.pack(expand = True,fill=BOTH)

        self._frame_student_on_que_quick=Frame(self._frame_class)
        self._frame_student_on_que_quick.pack(side = LEFT, expand=True, anchor = N,fill = X)

        self._frame_student_on_que_long=Frame(self._frame_class)
        self._frame_student_on_que_long.pack(side = LEFT, expand=True, anchor = N,fill = X)




    def queue_update(self):
        """Function which initiate the update of student's time on the queue"""
        self.update_frame_quick()
        self.update_frame_long()

        self.update_student_quick()
        self.update_student_long()


    def validation_quick(self):
        """Function which enables the user to join the queue and check is the name is valid as well as hanling any input error"""


        self._text_entry = simpledialog.askstring('Student ID', 'Enter your name to join the queue')

        self._texted_entry_quick= self._text_entry

        try:
            # check if this is a valid name with greater or equal than two characher eg: Xi, Michael...
            if len(self._texted_entry_quick) >= 2:

                # checking whether there are students already on the queue
                if len(STUDENT_LIST_TEMP_QUICK)>0:

                    # making sure this student is not joining both the queue and the same queue at the same time
                    if self._texted_entry_quick not in STUDENT_LIST_TEMP_QUICK and self._texted_entry_quick not in STUDENT_LIST_TEMP_LONG:

                        # find the number of time the student has asked for help since the opening of the app
                        student_question = STUDENT_LIST_QUICK.count(self._texted_entry_quick)

                        STUDENT_LIST_TEMP_QUICK.append(self._texted_entry_quick)

                        # the student number on the queue
                        student_num_quick =len(STUDENT_LIST_TEMP_QUICK)

                        join_time = time.time()

                        # instatiate a student object form StudentEntry frame class
                        student_entry_quick = StudentEntry(self._frame_student_on_que_quick, student_num_quick,
                                                     self._texted_entry_quick, student_question,join_time, 'a few seconds ago')
                        student_entry_quick.pack(expand = True,fill=X,pady = 2)
                        #store this student object in a permanent dictionary for future use
                        STUDENT_DICT_QUICK[self._texted_entry_quick] = (student_entry_quick, join_time)

                        #store this student object in a temporty dictionary to track their activity on the queue
                        STUDENT_DICT_TEMP_QUICK[self._texted_entry_quick] = (student_entry_quick, join_time)

                else:
                     # making sure this student is not joining both the queue and the same queue at the same time
                    if  self._texted_entry_quick not in STUDENT_LIST_TEMP_LONG:



                        student_question = STUDENT_LIST_QUICK.count(self._texted_entry_quick)


                        student_num_quick =1

                        STUDENT_LIST_TEMP_QUICK.append(self._texted_entry_quick)
                        join_time = time.time()

                        student_entry_quick = StudentEntry(self._frame_student_on_que_quick, student_num_quick,
                                                     self._texted_entry_quick, student_question,join_time, 'a few seconds ago')
                        student_entry_quick.pack(expand = True,fill=X, pady = 2)
                        #self._student_dict_quick[self._text_entry] = self._frame_student_student_num_quick
                        STUDENT_DICT_QUICK[self._text_entry] = (student_entry_quick, join_time)
                        STUDENT_DICT_TEMP_QUICK[self._text_entry] = (student_entry_quick, join_time)
        except:
            pass


    def validation_long(self):
        """Function which enables the user to join the long help queue and check is the name is valid as well as handling any input error"""

        self._text_entry = simpledialog.askstring('Student ID', 'Enter your name to join the queue')
        self._texted_entry_long=self._text_entry

        try:
            # check if this is a valid name with greater or equal than two characher eg: Xi, Michael...
            if len(self._texted_entry_long) > 2:

                # checking whether there are students already on the queue
                if len(STUDENT_LIST_TEMP_LONG)>0:

                    # making sure this student is not joining both the queue and the same queue at the same time
                    if self._texted_entry_long not in STUDENT_LIST_TEMP_LONG  and self._texted_entry_long not in STUDENT_LIST_TEMP_QUICK: # making sure this student is not joining both the queue and the same queue at the same time

                        # find the number of times the student has asked for help since the opening of the app
                        student_question = STUDENT_LIST_LONG.count(self._texted_entry_long)

                        STUDENT_LIST_TEMP_LONG.append(self._texted_entry_long)

                        # the student position on the queue
                        student_num_long = len(STUDENT_LIST_TEMP_LONG)

                        join_time = time.time()

                        # instatiate a student object from StudentEntry frame class
                        student_entry_long = StudentEntry(self._frame_student_on_que_long, student_num_long,
                                                     self._texted_entry_long, student_question,join_time ,'a few second ago')
                        student_entry_long.pack(expand = True,fill=X, pady = 2)
                        #self._student_dict_quick[self._text_entry] = self._frame_student_student_num_quick
                        STUDENT_DICT_LONG[self._texted_entry_long] = (student_entry_long, join_time)
                        STUDENT_DICT_TEMP_LONG[self._texted_entry_long] = (student_entry_long, join_time)

                else:
                    # making sure this student is not joining both the queue and the same queue at the same time

                    if  self._texted_entry_long not in STUDENT_LIST_TEMP_QUICK:

                        student_question = STUDENT_LIST_LONG.count(self._texted_entry_long)


                        student_num_long =1

                        STUDENT_LIST_TEMP_LONG.append(self._texted_entry_long)
                        join_time = time.time()

                        student_entry_long = StudentEntry(self._frame_student_on_que_long, student_num_long,
                                                     self._texted_entry_long, student_question,join_time, 'a few second ago')
                        student_entry_long.pack(expand = True,fill=X, pady =2)
                       #store this student object in a permanent dictionary for future use
                        STUDENT_DICT_LONG[self._text_entry] = (student_entry_long, join_time)

                        #store this student object in a temporty dictionary to track their activity on the queue
                        STUDENT_DICT_TEMP_LONG[self._text_entry] = (student_entry_long, join_time)
        except:
            pass


    def update_student_quick(self):
        """A function which update the time duration of the student on the quick help queue after joining"""

        # deleting the existing time difference in the queue
        del LABEL_LIST_TIME_QUICK[:]

        # making sure that there are student on the queue
        if len(STUDENT_LIST_TEMP_QUICK)> 0:
            for name in STUDENT_DICT_QUICK:

                # confirming if this student is on the queue
                    if name in STUDENT_DICT_TEMP_QUICK:
                        studentEntry, time_join = STUDENT_DICT_QUICK[name][0], STUDENT_DICT_QUICK[name][1]
                        time_now = time.time()
                        time_diference = time_now-time_join
                        LABEL_LIST_TIME_QUICK.append(time_diference)
                        if time_diference < 60:
                            studentEntry.set_time('a few second ago')


                        elif time_diference < 120:
                            studentEntry.set_time('a minute ago')


                        elif time_diference  < 3600:
                            timely = int(time_diference//60)
                            string_minutes = ' minutes ago'
                            studentEntry.set_time(f'{timely} {string_minutes}')



                        elif time_diference < 7200:
                            studentEntry.set_time('1 hour ago')

                        elif time_diference >= 7200:
                            timely = int(time_diference//3600)
                            string_minutes = ' hours ago'
                            studentEntry.set_time(f'{timely} {string_minutes}')

    def sort_student_quick(self):
        """Sorting the students frame on the queue starting with the least number of questions asked
         Return:
             list_final(list<class|Frame>): a list which contains the frame of available students on the quick queue """

        list_time = []
        list_question = []
        list_final = []

        if len(STUDENT_LIST_TEMP_QUICK)> 0:
            for name in STUDENT_DICT_TEMP_QUICK:
                query_num, time_join = STUDENT_DICT_QUICK[name][0].get_question(), STUDENT_DICT_QUICK[name][1]
                list_question.append(query_num)
                list_time.append(time_join)
            list_question.sort()
            list_time.sort()
            for query_day in list_question:
                for timely in list_time:
                    for student in STUDENT_DICT_QUICK:
                        if student in STUDENT_DICT_TEMP_QUICK:
                            if STUDENT_DICT_QUICK[student][0].get_question() == query_day and STUDENT_DICT_QUICK[student][0].get_time() == timely:
                                list_final.append(STUDENT_DICT_TEMP_QUICK[student][0])
            return list_final


    def update_frame_quick(self):
        """Method which updates the student's position in ascending order on the queue based on number of questions and time they join the queue
           eg: student with less questions asked will be given priority and iff they have the same number of questions longer time period is considered. """


        list_student_on_queue = []
        list_final = self.sort_student_quick()
        if list_final is not None:

            for student_mame in STUDENT_DICT_TEMP_QUICK:
                # removing all the avaible student on the queue before placing them again in order
                STUDENT_DICT_TEMP_QUICK[student_mame][0].pack_forget()


            for frame in list_final:
                frame.pack(fill = X)

            for frame_student in list_final:
                # removing mutli
                if frame_student.get_name() not in list_student_on_queue:
                    list_student_on_queue.append(frame_student.get_name())


            for student in list_student_on_queue: # assigning students their actual number on the queue
                if student in STUDENT_DICT_TEMP_QUICK:
                    numb = list_student_on_queue.index(student) + 1
                    STUDENT_DICT_QUICK[student][0].set_number(numb)




    def update_student_long(self):
        """A function which update the time duration of the student on the quick help queue after joining"""

        # deleting the existing time difference in the queue
        del LABEL_LIST_TIME_LONG[:]
        # making sure that there are student on the queue
        if len(STUDENT_LIST_TEMP_LONG)> 0:


            for name in STUDENT_DICT_LONG:

                # confirming if this student is on the queue
                if name in STUDENT_DICT_TEMP_LONG:
                    studentEntry, time_join = STUDENT_DICT_LONG[name][0], STUDENT_DICT_LONG[name][1]
                    time_now = time.time()
                    time_diference = time_now-time_join
                    LABEL_LIST_TIME_LONG.append(time_diference)
                    if time_diference < 60:
                        studentEntry.set_time('a few seconds ago')


                    elif time_diference < 120:
                        studentEntry.set_time('a minute ago')

                    elif time_diference  < 3600:
                        timely = int(time_diference//60)
                        string_minutes = ' minutes ago'
                        studentEntry.set_time(f'{timely} {string_minutes}')



                    elif time_diference < 7200:
                        studentEntry.set_time('1 hour ago')

                    elif time_diference >= 7200:
                        timely = int(time_diference//3600)
                        string_minutes = ' hours ago'
                        studentEntry.set_time(f'{timely} {string_minutes}')

    def sort_student_long(self):
        """Sorting the students frame on the long queue in ascending order starting with the least number of questions asked
        Return:
             list_final(list<class|Frame>): a list which contains the frame of available students on the long queue"""

        list_time = []
        list_question = []
        list_final = []


        if len(STUDENT_LIST_TEMP_LONG)> 0:
            for name in STUDENT_DICT_TEMP_LONG:
                # here we use the permenent dictionary and the actual key
                query_num, time_join = STUDENT_DICT_LONG[name][0].get_question(), STUDENT_DICT_LONG[name][1]
                list_question.append(query_num)
                list_time.append(time_join)
            list_question.sort()
            list_time.sort()
            for query_day in list_question:
                for timely in list_time:
                    for student in STUDENT_DICT_LONG:
                        if student in STUDENT_DICT_TEMP_LONG:
                            if STUDENT_DICT_LONG[student][0].get_question() == query_day and STUDENT_DICT_LONG[student][0].get_time() == timely:
                                list_final.append(STUDENT_DICT_TEMP_LONG[student][0])
            return list_final




    def update_frame_long(self):
        """Method which updates the student's position in ascending order on the queue based on number of questions and time they join the queue
           eg: student with less questions asked will be given priority and iff they have the same number of questions longer time period is considered. """

        list_student_on_queue = []
        list_final = self.sort_student_long()
        if list_final is not None:

            # removing all the avaible student on the queue before placing them again in order
            for student_mame in STUDENT_DICT_TEMP_LONG:
                STUDENT_DICT_TEMP_LONG[student_mame][0].pack_forget()

            for frame in list_final:
                frame.pack(fill = X)

            for frame_student in list_final:
                # removing multiple student names in this list
                if frame_student.get_name() not in list_student_on_queue:
                    list_student_on_queue.append(frame_student.get_name())


            for student in list_student_on_queue: # assigning students their actual number on the queue
                if student in STUDENT_DICT_TEMP_LONG:

                    #assigning position on the queue
                    numb = list_student_on_queue.index(student) + 1
                    STUDENT_DICT_LONG[student][0].set_number(numb)




## Adapted class from the internet:
##Link:  https://stackoverflow.com/questions/16188420/python-tkinter-scrollbar-for-frame

class UniFrameScroll(Frame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame
    * Construct and pack/place/grid normally
    * This frame only allows vertical scrolling

    """
    def __init__(self, parent):
        super().__init__(parent)
        """Construct vertical scroll to accommodate users as they join the queue with the parent frame
        Parameter:
            parent (tk.Tk|tk.Frame): The frame widget window whre the the scrollbar is packed.
            """

        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = Canvas(self, bd=0, highlightthickness=0,
                        yscrollcommand=vscrollbar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=canvas.yview)

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=NW)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)



class UniApp(object):
    """Toplevel application.
     The main app class which provide an interactive interface to the user joining the queue"""



    def __init__(self, master):

        """Construct a toplevel widget with the parent Master.
    Parameter:
        parent (tk.Tk|tk.Frame): The main window for the queuing  the application.
        """


        self.master = master
        self.master.title('CSSE1001 Queue')
        self.master.minsize(1000,600)

        self.frame = UniFrameScroll(self.master)
        self.frame.pack(expand = True, fill = BOTH)
        self.fame_game = ControlUniPrime(self.frame.interior)
        self.fame_game.pack(expand=True,fill = BOTH)
        self.button_frame = Frame(self.master, bg = '#fefbed',highlightbackground = '#fefbed',highlightthickness=2)
        self.button_frame.pack(fill = X)
        self.game_label = Label(self.button_frame, text = 'Click the "Play" button to play the game while waiting for help',fg='#C09853', bg ='#fefbed', font ='arial 18 bold')
        self.game_label.pack(side = LEFT, fill = X)

        self.button_start = Button(self.button_frame, text = 'Play',fg='#C09853',highlightbackground = '#fefbed',width = 10, height = 2,command = self.game_window)
        self.button_start.pack(side = RIGHT, anchor = W)






        self.poll()

    def poll(self):
        """A method which update the the student activities on the queue"""

        self.fame_game.control_uni.queue_update()
        self.fame_game.label_upadate()

        self.master.after(10000,self.poll)



    def game_window(self):
        """method which enables the Toplevel window of the game"""


        window_2 = Toplevel(self.master)

        game = GameApp(window_2)





## Adapted  from the internet:
##Link: https://www.youtube.com/watch?v=9tVCYIcwNjw

class GameApp(object):
    """Toplevel application.
     The main app class which provide an interactive interface to the user playing the game"""


    def __init__(self, master):
        """Construct a toplevel widget with the parent Master.
    Parameter:
        parent (tk.Tk|tk.Frame): The main window for the game application.
        """
        self.master = master
        self.master.title('Bouncing Ball Game')
        self.master.wm_geometry("600x500")
        self.master.wm_attributes("-topmost", 1)

        button_label_start = Frame(self.master, bg = '#fefbed',highlightbackground = '#fefbed',highlightthickness=2)
        button_label_start.pack(fill=X)
        self.start_label = Label(button_label_start, text = 'Welcome to bouncing Ball game',fg='#C09853', bg ='#fefbed', font ='arial 15 bold')
        self.start_label.pack(side = LEFT, fill = X)
        button_start= Button(button_label_start, text = 'Start Game',fg='#C09853',highlightbackground = '#fefbed',command = self.playing)
        button_start.pack(side = RIGHT)

        button_frame = Frame(self.master, bg = '#fefbed',highlightbackground = '#fefbed',highlightthickness=2)
        button_frame.pack(side = BOTTOM,fill=X)
        quit_label = Label(button_frame, text = 'Press the "Quit game" button to go back to the queue',fg='#C09853', bg ='#fefbed', font ='arial 15 bold')
        quit_label.pack(side = LEFT, fill = X)
        button_quit= Button(button_frame, text = 'Quit Game', fg='#C09853',highlightbackground = '#fefbed',command = self.quit_game)
        button_quit.pack(side=RIGHT)
        canvas_frame= Frame(self.master,highlightbackground = 'light blue')
        canvas_frame.pack()

        self.canvas = Canvas(canvas_frame,width = 600, height = 500, bg = 'light blue')
        self.canvas.pack()
        self.master.update()

        self.paddle = Paddle(self.canvas,'#3c763d')
        self.ball = Ball(self.canvas,self.paddle,'gold2')


        self.is_valid = True






    def playing(self):
        """A method which invonkes the game"""
        self.start_label.config(text = 'The game has started press left or right arrow key', fg = 'green',font ='arial 15 bold')

        self.time_join = time.time()

        while self.is_valid:
            if self.ball.hit_bottom == False:
                self.ball.draw_ball()
                self.paddle.draw()
                self.master.update_idletasks()
                self.master.update()
                time.sleep(0.01)
            else:
                duration_game = int(time.time() - self.time_join)
                if duration_game < 60:
                    messagebox.showinfo('Game Over',f"Your game lasted for {duration_game} second, check the status of the queue and play again if you would like to")

                    self.is_valid = not self.is_valid
                    self.master.destroy()


                else:
                    game_time = duration_game//60
                    messagebox.showinfo('Game Over',f"Wow!! {game_time} munites is a good trial.")


                    self.is_valid = not self.is_valid
                    self.master.destroy()


    def quit_game(self):
        """A method which quick the the game and closes the window"""
        self.is_valid = not self.is_valid

        self.master.destroy()







class Ball(object):
    """A moving class which enable the movement of the ball after it is drawn on canvas """
    def __init__(self,canvas,paddle,colour):
        """
        Constructor

        Parameters:
            paddle (class< paddle class>): the paddle which will be catching the bouncing ball.
            canvas (class(Canvas <dict<*, *>)): Keyword arguments for tk.Canvas.
            colour(str): colour of the ball
        """
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10,10,25,25,fill = colour)
        self.canvas.move(self.id,245,100)

        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False


    def hit_paddle(self, pos):
        """Returns True iff the ball hit the paddle otherwise False.
        Return:
            bool(True): return True when the ball hit the paddle otherwise False.
            """

        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True

        return False

    def draw_ball(self):
        """Enables and facilitates the motion of the ball on the canvas."""
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 2
        elif pos[3] >= self.canvas_height:
            self.hit_bottom = True

        elif self.hit_paddle(pos)== True:
            self.y = -2

        elif pos[0] <= 0:
            self.x = 2

        elif pos[2] >= self.canvas_width:
            self.x = -2

class Paddle(object):
    """A Paddle class which draws and enables the motion of the paddle on the canvas using the arrow keys."""
    def __init__(self,canvas,colour):
        """
        Constructor

        Parameters:

            canvas (class(Canvas <dict<*, *>)): Keyword arguments for tk.Canvas.
            colour(str): colour of the paddle.
        """
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill = colour)
        self.canvas.move(self.id,200,300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)


    def draw(self):
        """Enables and facilitates the motion  of the paddle in both left or right on the canvas."""
        self.canvas.move(self.id, self.x,0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >=self.canvas_width:
            self.x = 0

    def turn_left(self,evt):
        """Changing the direction of the paddle to left"""
        self.x = -2
    def turn_right(self,evt):
        """Changing the direction of the paddle to right"""
        self.x = 2





if __name__=='__main__':
    window = Tk()

    app = UniApp(window)
    window.mainloop()


