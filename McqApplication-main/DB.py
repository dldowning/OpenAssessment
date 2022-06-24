import mysql.connector as connector
import DesignColors
color=DesignColors.Fonts()

#CRUD OPERATIONS
''' 
CREATE (INSERT)
READ (SELECT)
UPDATE
DELETE
'''


class Dbhelper:
    def __init__(self):
        self.con=connector.connect(host='localhost',port='3306',user='root',password='T.srsdv123',database='mcquiz')
        #whenever the program executed created IF NOT EXISTS. So if the table exists it will show the db table.
        query='CREATE TABLE if not exists user(UserId int primary key,UserName varchar(20),Password varchar(20))'
        #creating cursor. This will execute queries.
        cur=self.con.cursor()
        cur.execute(query)
    
    #insert
    def insert_user(self,userid,username,password):
        query="INSERT INTO user VALUES({},'{}','{}')".format(userid,username,password)
        cur = self.con.cursor()
        cur.execute(query)
        #Commit means changing in database physically or really.
        #if we dont use commit() then it will only show output in cmd but the real db did not get changed. Thats why we have to use commit
        self.con.commit()
        print('User Saved To Database')

    #Fetch ALL
    def fetch_all(self):
        query='SELECT * FROM user'
        cur=self.con.cursor()
        cur.execute(query)
        for row in  cur:  
            print('User Id:',row[0])
            print('User Name:',row[1])
            print('Password:',row[2])
            print()
            print()
    
    #Fetch One
    def fetch_one(self,id):
        query='SELECT * FROM user WHERE userId={}'.format(id)
        cur=self.con.cursor()
        cur.execute(query)
        for row in  cur:  
            print('User Id:',row[0])
            print('User Name:',row[1])
            print('Password:',row[2])
    
    #Delete User
    def delete_user(self,id):
        query='DELETE FROM user WHERE userID={}'.format(id)
        cur=self.con.cursor()
        cur.execute(query)
        #Commit means it will delete the record in database physically or really.
        self.con.commit()
        print('User Record Deleted.')
    
    #Update
    def update_user(self,userid,newname,newpassword):
        query="UPDATE user set userName='{}',password='{}' WHERE userId={}".format(newname,newpassword,userid)
        cur=self.con.cursor()
        cur.execute(query)
        #Commit means it will Update the record in database physically or really.
        self.con.commit()
        print('User Record Updated.')
    
    def checkuser(self,un,p):
        query="SELECT * FROM user where UserName='{}' AND Password='{}'".format(un,p)
        cur=self.con.cursor()
        cur.execute(query)
        for row in  cur:  
            print('Welcome User:',row[1])
            return 1
            break
        else:
            print('Invalid User!')
            return 0


class Quizhelper():
    def __init__(self):
        self.con=connector.connect(host='localhost',port='3306',user='root',password='T.srsdv123',database='mcquiz')
        #whenever the program executed created IF NOT EXISTS. So if the table exists it will show the db table.
        query='CREATE TABLE if not exists quiz(QueNo int primary key,Question VARCHAR(100),Difficulty VARCHAR(30),OptionA VARCHAR(30),OptionB VARCHAR(30),OptionC VARCHAR(30),OptionD VARCHAR(30),Answer int,Topic VARCHAR(30))'
        #creating cursor. This will execute queries.
        cur=self.con.cursor()
        cur.execute(query)
    
    #insert
    def insert_quiz(self,queno,ques,diff,opta,optb,optc,optd,ans,topic):
        query="INSERT INTO quiz VALUES({},'{}','{}','{}','{}','{}','{}',{},'{}')".format(queno,ques,diff,opta,optb,optc,optd,ans,topic)
        cur = self.con.cursor()
        cur.execute(query)
        #Commit means changing in database physically or really.
        #if we dont use commit() then it will only show output in cmd but the real db did not get changed. Thats why we have to use commit
        self.con.commit()
        print('Question Saved To Database')
    # this method fetches the quiz from the database
    def fetch_quiz(self):
        query='SELECT * FROM quiz'
        cur=self.con.cursor()
        cur.execute(query)
        for row in  cur:  
            print('Question No:',row[0])
            print('Question:',row[1])
            print('Difficulty:',row[2])
            print('Topic Name:',row[8])
            print('Option 1:',row[3])
            print('Option 2:',row[4])
            print('Option 3:',row[5])
            print('Option 4:',row[6])
            print('Answer:',row[7])
            print()
            print()

class User_Quiz():
    def __init__(self):
        self.con=connector.connect(host='localhost',port='3306',user='root',password='T.srsdv123',database='mcquiz')
        #whenever the program executed created IF NOT EXISTS. So if the table exists it will show the db table.
        query='CREATE TABLE if not exists player(PlayerName varchar(20),Score int)'
        #creating cursor. This will execute queries.
        cur=self.con.cursor()
        cur.execute(query)

    def fetch_que(self,pname,s):
        query='INSERT INTO player VALUES("{}",{})'.format(pname,s)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()

        querytopic='SELECT DISTINCT(Topic) FROM quiz'
        cur=self.con.cursor()
        cur.execute(querytopic)
        print('Kindly Select Topic for the quiz')
        for i in cur:
            print(i[0])
        inp=input('Enter Topic: ')
        print()
        que='SELECT * FROM quiz WHERE Topic="{}"'.format(inp)
        cur=self.con.cursor()
        cur.execute(que)
        score=0
        for row in  cur:  
            print(color.BOLD + color.PURPLE +'Que:',row[0],'>','Question:',row[1])
            print(color.BOLD + color.YELLOW +'Option 1:'+color.END,row[3])
            print(color.BOLD + color.YELLOW +'Option 2:'+color.END,row[4])
            print(color.BOLD + color.YELLOW +'Option 3:'+color.END,row[5])
            print(color.BOLD + color.YELLOW +'Option 4:'+color.END,row[6])
            print()
            num=int(input(color.BOLD + color.GREEN +'Enter the correct option: '+color.END))
            if row[2].lower()=='easy':
                if num==row[7]:
                    score+=2
            else:
                if num==row[7]:
                    score+=5
        query1="UPDATE player SET Score={} WHERE PlayerName='{}'".format(score,pname)
        cur=self.con.cursor()
        cur.execute(query1)
        self.con.commit()
        print()
        print(color.BOLD + color.RED+'******YOUR RESULT********'+color.END)
        print(color.BOLD + color.DARKCYAN +"Student: "+color.END,pname)
        print(color.BOLD + color.GREEN +"Score: "+color.END,score)
        print()
        want=input('Do You Want to see Solutions ? Press 0 to exit | Press Any key to see Solutions: ')
        if want!='0':
            que='SELECT * FROM quiz WHERE Topic="{}"'.format(inp)
            cur=self.con.cursor()
            cur.execute(que)
            print()
            print('The correct Answers are')
            for row in cur:
                print(color.BOLD + color.PURPLE +'Que:',row[0],'>','Question:',row[1])
                print(color.BOLD + color.YELLOW +'Option 1:'+color.END,row[3])
                print(color.BOLD + color.YELLOW +'Option 2:'+color.END,row[4])
                print(color.BOLD + color.YELLOW +'Option 3:'+color.END,row[5])
                print(color.BOLD + color.YELLOW +'Option 4:'+color.END,row[6])
                print(color.BOLD + color.GREEN+'ANSWER FOR GIVEN QUESTION IS: '+color.END,row[7])
                print()

# displays the score of the user who took the quiz
class ShowUserScore():
    def __init__(self):
        self.con=connector.connect(host='localhost',port='3306',user='root',password='T.srsdv123',database='mcquiz')
        query='SELECT PlayerName,Score FROM player ORDER BY Score DESC'
        cur=self.con.cursor()
        cur.execute(query)
        for row in  cur:  
            print(color.BOLD + color.YELLOW+'Player Name:'+color.END,row[0])
            print(color.BOLD + color.GREEN+'Player Score:'+color.END,row[1])
            print()
            print()