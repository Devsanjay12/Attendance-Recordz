# ATTENDANCE REPORTER
# created on 3 dec 2023 - modified on 15 dec 2023.
# ©Devsanjay12 - github

# importing functions
import datetime

ddn = datetime.datetime.now()

# STUDENTS NAMES---ACADAMIC YEAR 2020 ---

# CLASS IT 1
stuIT1 = set(
    [
        "Raghava",
        "Amarnath A",
        "Cathirinblessy A",
        "Paul Abisheike P",
        "Reagan Benny C",
        "Harshini C V",
        "Yuthish C",
        "Pruthvi Dinesh",
        "Sreekarthika G",
        "Krittika Gahlot",
        "Sathiyaseelan J",
        "Hariharan K S",
        "Vishwas Kumar",
        "Atheeswaran M",
        "Nikhil M",
        "Prasanth M",
        "Tarushi Marchino",
        "Dharshini Muthubala P",
        "Ashoknarayanan N",
        "Akash Nair",
        "Vishnu P Nair",
        "Mukund P U",
        "Atul Prakash",
        "Kalaitharan R",
        "Poezhilan R",
        "Poorvekka R",
        "Sreeraam R",
        "Dhanushkumar S",
        "Pooja S G",
        "Gopinath S",
        "Priyadarsan S",
        "Sarvesh S",
        "Poluribalaji Sandeep",
        "Piyush Singh",
        "Jahnavi Sinha",
        "Sharmikkhashri T",
        "Prithivi Ram V",
        "Vijayasaran V",
    ]
)

# CLASS IT 2
stuIT2 = set(
    [
        "RAMYA A L",
        "MAYANK ANAND JHA",
        "STEPHEN ANESH",
        "SABARISREE C",
        "VARSHASRI C",
        "SANJANA CHAUHAN",
        "GRIESELDA CHRIS J P",
        "KAVINMOZHI D",
        "ASWIN DANIEL N P",
        "SAKSHI DAYASHANKAR",
        "RAHNA FARHIN A",
        "DHIVYADHARSHINI G",
        "GOKUL G",
        "MAHITHA G",
        "THANUSHREE G T",
        "ROHITH GANESH G",
        "ACCHUTHAN K",
        "KANISHKA K",
        "KAVINRAJ K R",
        "SHREEHARINI K",
        "ADITI KUMARI",
        "SAKTHIRAGUL L",
        "PRAVINA M B",
        "RAGULKUMAR M",
        "SAGANA M",
        "INDRALAKSHMI N",
        "MADHUSHREE N",
        "SREELAKSHMI N",
        "VAISHAK N",
        "GOKUL NILAVAN E",
        "DHANUSHREE P K",
        "SUBATHRA P S",
        "DEEPTHI P SREEGANTHAN",
        "DEEPTEE PANDEY",
        "ARCHIT PARASHAR",
        "AISHVARYA R",
        "KETHAN R S",
        "Aniket Ray",
        "ABINAYA S",
        "ANEESH S",
        "ARCHANADEVI S",
        "ADHISHANKAR S B",
        "DARSAN S",
        "DEEPTHI S",
        "JANANI S",
        "CHARUSHREE S K",
        "PRIYADARSINI S K",
        "LINNESH S",
        "MONISHHA S",
        "MAHESWARAN S R",
        "SAHANA S",
        "JESSICA SEBASTIAN",
        "BIBINE SELVA",
        "ADITYA SINGH",
        "LALITHA SUDHARSANA M",
        "SUGESH V",
        "JANAPRABHAKAR A",
    ]
)

# CLASS IT 1
stuIT1 = set(
    [
        "Jaison A",
        "Kathir A",
        "Mohd.Ajmal A",
        "Naveen A",
        "Vijayendar A",
        "Shreya Ann Kuruvilla",
        "Anjana B G",
        "Pranave B",
        "Priyanandhine B",
        "Yureaka B",
        "Abinantha G R",
        "Shradha G",
        "Keerthana H",
        "Nikhitha J Gireesh",
        "Vishwanath J M",
        "Anjali Devi K",
        "Krishnapriya K M",
        "Ashish Kumar",
        "Abhinivesh M",
        "Lithika M",
        "Mailesh M",
        "Malavika M",
        "Mathan Kumar M",
        "Mukesh M",
        "Vinotha M",
        "Vishva bharath M",
        "Abin Mathew",
        "Keerthana N",
        "Naresh Kumar N",
        "Swetha N",
        "Priyadharshini P C",
        "Nandini P",
        "Shubash P",
        "Harish Prasanth",
        "Athira R",
        "Kanchana Devi R R",
        "Surya Kumar R",
        "Vaseemah R",
        "Supreeth Ragavendra",
        "Mrudubashini Ramathan",
        "Devaki S",
        "Harshini S",
        "Sam Sebas S",
        "Varshini S",
        "Sakthi Sakthi",
        "Vignesh Sarat",
        "Samik Sarkar",
        "Kiruthika T",
        "Rakesh T",
        "Akshara Saradha V",
        "Kavishri V",
        "Shriram V",
    ]
)


# PLEASE DONT CHANGE ANYTHING BELOW THIS.
# creating functions
def mainlooping():
    stu_present_list = []
    while True:
        data = input()
        if str.lower(data) == "zzz":
            break
        stu_present_list.append(data)

    # conversion
    low_all_names = set([x.lower() for x in all_names])
    len_low_all_names = len(low_all_names)

    low_stu_present_list = set([x.lower() for x in stu_present_list])
    len_low_stu_present_list = len(low_stu_present_list)

    # comparison
    absentees_names = low_all_names.difference(low_stu_present_list)
    stu_absent = len(absentees_names)

    print(
        "============================================================================"
    )
    print("\n\nNOTE : THIS IS COMPUTER GENERATED ABSENTEES LIST REPORTED ON:- ", ddn)
    if userask == 1:
        print("\nYOU HAVE SELECTED THE NAMES OF STUDENTS OF CLASS IT 1.")
    elif userask == 2:
        print("\nYOU HAVE SELECTED THE NAMES OF STUDENTS OF CLASS IT 2.")
    elif userask == 3:
        print("\nYOU HAVE SELECTED THE NAMES OF STUDENTS OF CLASS IT 3.")
    elif userask == 4:
        print("\nYOU HAVE SELECTED THE NAMES OF STUDENTS OF CLASS IT 1 and IT 2.")
    elif userask == 5:
        print("\nYOU HAVE SELECTED THE NAMES OF STUDENTS OF CLASS IT 2 and IT 3.")
    elif userask == 6:
        print("\nYOU HAVE SELECTED THE NAMES OF STUDENTS OF CLASS IT 3 and IT 1.")
    elif userask == 7:
        print("\nYOU HAVE SELECTED ALL THE STUDENTS OF CLASS IT.")

    elif userask == 8:
        print("\nYOU HAVE SELECTED THE NAMES OF STUDENTS OF CLASS CSE 2.")
    elif userask == 9:
        print("\nYOU HAVE SELECTED THE NAMES OF STUDENTS OF CLASS CSE 2.")
    elif userask == 10:
        print("\nYOU HAVE SELECTED THE NAMES OF STUDENTS OF CLASS CSE 3.")
    elif userask == 11:
        print("\nYOU HAVE SELECTED THE NAMES OF STUDENTS OF CLASS CSE 1 and 2.")
    elif userask == 12:
        print("\nYOU HAVE SELECTED THE NAMES OF STUDENTS OF CLASS CSE 2 and 3.")
    elif userask == 13:
        print("\nYOU HAVE SELECTED THE NAMES OF STUDENTS OF CLASS CSE 3 and 1.")
    elif userask == 14:
        print("\nYOU HAVE SELECTED ALL THE STUDENTS OF CLASS CSE.")

    llal1 = str(len_low_all_names)
    llstl2 = str(len_low_stu_present_list)
    stabs = str(stu_absent)
    absna = str(absentees_names)
    p1n = str("\n***Total number of students:- " + llal1)
    p2st = str("***To number of students present:- " + llstl2)
    p3sa = str("***Total number of students absent:- " + stabs)
    p4an = str("\n***Absentees names:- " + absna)
    print(p1n)
    print(p2st)
    print(p3sa)
    print(p4an)

    # file handing (.txt)
    ddn1 = str(ddn)
    fhs = "DATED_" + ddn1 + ".txt"
    ffh = open(fhs, "a")
    ffh.write(p1n)
    ffh.write("\n")
    ffh.write(p2st)
    ffh.write("\n")
    ffh.write(p3sa)
    ffh.write("\n")
    ffh.write(p4an)
    ffh.write("\n")
    copyright1 = str("\n© Designed and Programmed by Sanjay Kumar")
    ffh.write(copyright1)
    ffh.close()
    print("\nYour absentees report is saved in location,")
    print("/Users/sanjaykumar./Documents/PYTHON/ATTENDANCE REPORT FILES/")
    print(copyright1)


# ======main loop============
userask = int(
    input(
        """SELECT THE CLASSES:-
[press 1] - IT 1
[press 2] - IT 2
[press 3] - IT 3
[press 4] - IT 1 and 2
[press 5] - IT 2 and 3
[press 6] - IT 3 and 1
[press 7] - ALL SECTIONS OF CLASS IT (ie; 1,2 and 3):- """
    )
)


if userask == 1:
    all_names = stuIT1
    mainlooping()

elif userask == 2:
    all_names = stuIT2
    mainlooping()

elif userask == 3:
    all_names = stuIT3
    mainlooping()

elif userask == 4:
    all_names = stuIT1.union(stuIT2)
    mainlooping()

elif userask == 5:
    all_names = stuIT2.union(stuIT3)
    mainlooping()

elif userask == 6:
    all_names = stuIT3.union(stuIT1)
    mainlooping()

elif userask == 7:
    stuIT1_b = stuIT1.union(stuIT2)
    all_names = stuIT1_b.union(stuIT3)
    mainlooping()

elif userask > 14:
    print("\nINVALID USER INPUT WHILE CHOOSING CLASSES.")
