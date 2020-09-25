#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

g_joint_hypermobility = 0 # General joint hypermobility 0
l_joint_hypermobility = 0 # Localized to single joints hypermobility 1
p_joint_hypermobility = 0 # Limited to hands or feet hypermobility 2
h_joint_hypermobility = 0 # Historical joint hypermobility 3

# Variables for Classical EDS
cEDS = 0 # 4
major_cEDS = 0 # This signales skin involvment 5
minor_cEDS = 0 # 6

# Variables for Classical-like EDS
clEDS = 0 # 7
major_clEDS = 0 # 8 
minor_clEDS = 0 # This is for family history 9

# Variables for Cardiovascular EDS 
cvEDS = 0 # 10
major_cvEDS = 0 # 11
major2_cvEDS = 0 # 12
minor_cvEDS = 0 # 13

# Variables for Vascular EDS
vEDS = 0 # 14
true_major_vEDS = 0 # 15
major_vEDS = 0 # 16

# Variables for Hypermobile EDS
hEDS = 0 # 17
featureA_hEDS = 0 # 18
featureB_hEDS = 0 # 19
featureC_hEDS = 0 # 20

# Variables for Athrochalasia EDS
aEDS = 0 # 21
major_aEDS = 0 # 22
joint_complication_aEDS = 0 # 23
major2_aEDS = 0 # 24
minor_aEDS = 0 # 25

# Variables for Dermatosparaxis EDS
dEDS = 0 # 26
major_dEDS = 0 # 27
major2_dEDS = 0 # 28
minor_dEDS = 0 # 29

# Variables for Kyphoscoliotic EDS
kEDS = 0 # 30
major_kEDS = 0 # 31
joint_complication_kEDS = 0 # 32
minor_kEDS = 0 # 33

# Variables for Brittle Cornea Syndrome
BCS = 0 # 34
major_BCS = 0 # 35
major2_BCS = 0 # 36
minor_BCS = 0 # 37

# Variables for Musculocontractural EDS
mcEDS = 0 # 38
major_mcEDS = 0 # 39
major2_mcEDS = 0 # 40

# Variables for Myopathic EDS
mEDS = 0 # 41
major_mEDS = 0 # 42
major2_mEDS = 0 # 43
minor_mEDS = 0 # 44
hypermobility_distal_joint = 0 # 45

# Variables for Periodontal EDS
pEDS = 0 # 46
major_pEDS = 0 # 47
major2_pEDS = 0 # 48
minor_pEDS = 0 # 49

# Variables for Spondylodysplastic
spEDS = 0 # 50
major_spEDS = 0 # 51
radiology_spEDS = 0 # 52
minor_spEDS = 0 # 53

# Variables for Asymptomatic Generalized Joint Hypermobility
GJH = 0 # 54

# Variables for Asymptomatic Localized Joint Hypermobility
LJH = 0 # 55

# Variables for Asymptomatic Peripheral Joint Hypermobility
PJH = 0 # 56

# Variables for Generalized Hypermobility Spectrum Disorder
G_HSD = 0 # 57
major_GHSD = 0 # 58

# Variables for Localized Hypermobility Spectrum Disorder
L_HSD = 0 # 59
major_LHSD = 0 # 60

# Variables for Peripheral Hypermobility Spectrum Disorder
P_HSD = 0 # 61
major_PHSD = 0 # 62

# Variables for Historical Hypermobility Spectrum Disorder
H_HSD = 0 # 63
major_HHSD = 0 # 64

# Variables for Loeys-Dietz Syndrome
LDS = 0 # 65
major_LDS = 0 # 66

# Variables for Marfan Syndrome
marfan = 0 # 67
major_marfan = 0 # 68
fam_marfan = 0 # 69
mut_marfan = 0 # 70
ectopia_marfan = 0 # 71
aorta_marfan = 0 # 72


# In[2]:


# In[2]:


questions = ['Does the patient currently have or historically had joint hypermobility (joints that have a wider range of motion)? This can be generalized or limted to a single joint. ',
          'Does the patient experience muscular or joint abnormalities? EX: Muscle weakness or joint pain ',
           'Has the patient experienced skeletal or bone abnormalities? EX: Short stature, arachnodactyly, or foot deformities ',
           'Does the patient experience skin related abnormalities? EX: Easy bruising, skin tearing, or skin hyperextensibility ',
           'Has the patient demonstrated arterial or vascular fragility/abnormalities? EX: Aneurysms ',
           'Does the patient demonstrate organ/connective tissue fragility? EX: Hernia or prolapse ',
           'Has the patient experienced problems related to your eyes or vision? EX: Nearsighted or lens dislocation ',
          'Has the patient experienced mouth or denture abnormalities? EX: Split uvula or tooth abnormalities ',
           'Was the patient born with or have they developed distinct facial characteristics? EX: Widely spaced eyes ',
            'Has the patient experienced any developmental or growth delays? EX: Postnatal growth retardation or delayed cognitive development ',
            'Does the patient have a family history of heritable connective tissue disorders or have you been genetically tested for one? EX: Brother is diagnosed with Marfan Syndrome '
          ]


# In[3]:


# -1 = yes to previous question about muscle hypotonia
# -2 = ask question targeted at female
# -3 = ask question targeted at hypermetropia and myopia
# -4 = skin hyperextensibility A
# -5 =  palmar wrinkling A
# -6 =  atrophic scar A
# -7 =  bruising A
# -8 =  facial assymetry B
# -9 =  large fonatnelle B
# -10 =  downslanting palpebral fissure B
    

# In[68]:

import time

def intro():
    print('Welcome to Connect the DOTS, a symptom checker for Heritable Connective Tissue Disorders or HCTDs.')
    print('Please be patient while the informtation loads. It might take a second.')
    print('**************************************************************************************************')
    time.sleep(4)
    skip_intro = input('Would you like to skip the introduction and dislcaimer? Please answer yes if you would like to skip and no if you would like to continue. By answering yes you agree to the terms and services. ')
    while not(skip_intro.lower() == 'yes' or skip_intro.lower() == 'no'):
        skip_intro = input('Please answer yes or no.')
    if skip_intro.lower() == 'no':
        print('HCTDS are disorders and syndromes that affect the connective tissue in your body. Examples of connective tissue include skin, joints, muscles, and blood vessels.')
        time.sleep(5)
        print('DOTS specifically tests for the 22 most common and relatively misdiagnosed conditions in an attempt to help patients determine their likely diagnosis in a shorter period of time and with greater ease.')
        time.sleep(4)
        print('These 22 conditions include Marfan Syndrome, Loeys-Diets Syndrome, the Ehlers-Danlos Syndromes, and the Hypermobility Spectrum Disorders.')
        time.sleep(4)
        print('DOTS will ask you a series of questions about your symptoms to get a better idea of your health and which connective tissue disorder best matches your symptoms. Please answer as honestly as possible to get the most accurate results.')
        time.sleep(6)
        print('If you are uncertain about the answer to a question, respond with "idk". However, in most cases, though not always, individuals will be familiar with the condition/symptom if they are diagnosed with it. Please only respond with "yes", "no" or "idk" to questions unless prompted otherwise.')
        time.sleep(3)
        print('This questionnaire should take no more then 20 minutes. Thank you for participating in DOTS, we will ask you a few general question before getting started.')
    if skip_intro.lower() == 'yes':
        print('Okay, we will now ask you a few general questions about your health before we get started. Please answer as honestly as possible.')
        time.sleep(4)
        print('Thank you for participating in DOTS.')
        time.sleep(2)


# In[3]:


def get_patient_info():
    age = input("What is the patient's age? Please only respond with a number. ")
    age = int(age)
    print('The patient is ', age,' years old.')
    correct_age = ask_question('Is this correct? ')
    while correct_age.lower() == 'no':
        print("Please rewrite the patient's age. Make sure to only use numbers.")
        age = input("What is the patient's age? ")
        print('The patient is ', age, ' years old.')
        correct_age = input('Is this correct? ')
    if correct_age.lower() == 'yes':
        print('Okay, one last question before we begin.')
    sex = input("What is the patient's biological sex? Please answer male or female. ")
    while not(sex.lower() == 'female' or sex.lower() == 'male'):
        sex = input('Please answer male or female.')
    print('The patient is biologically a ', sex, '.')
    correct_sex = ask_question('Is this correct? ')
    while correct_sex.lower() == 'no':
        print("Please rewrite the patient's biological sex. Please answer male or female. ")
        sex = input("What is the patient's biological sex? Please answer male or female. ")
        print('The patient is biologically a ', sex, '.')
        correct_sex = input('Is this correct? ')
    if correct_sex.lower() == 'yes':
        print('We will now be begin the questionnaire. Thank you for your patience.')
        print('********************************************************************')
        print('                                                                    ')
    time.sleep(3)
    return age, sex


# In[4]:


def ask_question(question):
    answer = input(question)
    while not(answer.lower() == 'yes' or answer.lower() == 'no' or answer.lower() == 'idk'):
        answer = input('Please answer yes, no, or idk.')
    return answer


# In[5]:


def get_questions(filename):
    questions_dict = {}
    with open(filename) as fp:
        for line in fp:
            line = line.strip()
            index = line.find(',')
            if len(line) != 0:
                questions_dict[line[:index]] = line[index + 1:]
    return questions_dict


# In[6]:


def get_systems():
    systems = [""]*len(questions)
    for i in range(len(questions)):
        systems[i] = input(questions[i]).lower()
        while not(systems[i].lower() in ['yes', 'no', 'idk']):
            systems[i] = input('Please answer yes, no, or idk.').lower()

    #Whatever said yes to will be continued in next part. At the end their will be addition of miscallaneous symptoms
    if 'yes' in systems or 'idk' in systems:
        print("Okay, we will now ask you specific questions about the patient's health based on your answers above.")
        print('****************************************************************************************************')
        time.sleep(3)
    return systems


# In[7]:


def special_cases(row, questions_dict, mc_eds_check, mc_eds_code, prev_answer):
    should_ask_question = False
    answer = 'no'
    code = int(row[0])
    if code == -1 or code == -3:
        if prev_answer == 'yes':
            row = row[1:]
            should_ask_question = True
    elif code == -2:
        if sex == 'female':
            row = row[1:]
            should_ask_question = True
    elif code == -14:
        if prev_answer == 'no':
            row = row[1:]
            should_ask_question = True
    elif code == -11:
        if age < 16:
            if variables[0] > 0.44 and variables[0] < 0.66:
                row = row[1:]
                should_ask_question = True
    elif code == -12:
        if age >= 16 and age <= 50:
            if variables[0] > 0.33 and variables[0] < 0.55:
                row = row[1:]
                should_ask_question = True
    elif code == -13:
        if age > 50:
            if variables[0] > 0.22 and variables[0] < 0.44:
                row = row[1:]
                should_ask_question = True
    else:
        should_ask_question = True
    if code in [-4, -5, -6, -7]:
        mc_eds_check = True
        mc_eds_code = 0
        row = row[1:]
    if code in [-8, -9, -10]:
        mc_eds_check = True
        mc_eds_code = 1   
        row = row[1:]
    if int(row[0]) == 11 and ('yes' in systems[1:] or 'idk' in systems[1:]):
        answer = ask_question(questions_dict[row[1]])
    elif should_ask_question == True:
        answer = ask_question(questions_dict[row[1]])
    return answer, row, mc_eds_check, mc_eds_code


# In[15]:


# In[7]:


#Step one: come up with an encoding scheme for special questions (should be int code)
#Step two: If statement early in the loop that check for special case. Ex. if int(row[0]) > len(systems) or < 0
def get_symptoms(filename, questions_dict, systems):
    with open(filename) as fp:
        prev_answer = 'yes'
        for line in fp:
            line = line.strip()
            mc_eds_check = False
            mc_eds_code = 0
            if line != "":
                row = line.split(",")

                if int(row[0]) == 11 and not ('yes' in systems[1:] or int(row[0]) == 11 and 'idk' in systems[1:]):
                    continue
                if int(row[0]) == 11 or (int(row[0]) < 0 and systems[int(row[1])] == 'yes') or (int(row[0]) >=0 and systems[int(row[0])] == 'yes'):
                    #Special Cases
                    answer, row, mc_eds_check, mc_eds_code = special_cases(row, questions_dict, mc_eds_check, mc_eds_code, prev_answer)
                    if answer == 'yes':
                        for i in range(2, len(row), 2):
                            if mc_eds_check and int(row[i]) == 40:
                                if mc_eds_code == 0 and age >= 10:
                                    variables[int(row[i])] += float(row[i + 1]) 
                                if mc_eds_code == 1 and age < 10:
                                    variables[int(row[i])] += float(row[i + 1])
                            else:
                                variables[int(row[i])] += float(row[i + 1])
                    prev_answer = answer
        return variables


# In[19]:


def requirements(variables, age):
    if age <  16 and variables[0] >= 0.66 and variables[5] == 1 or age >=  16 and age < 50 and variables[0] >= 0.55 and variables[5] == 1 or age >= 50 and variables[0] >= 0.44 and variables[5] == 1 or variables[5] == 1 and variables[6] >= 2.25:
        print('Based on your answers, the patient meets the minimal clinical criteria for Classical Ehlers-Danlos Syndrome. We recommend gene specific testing specifically targeted at the COL5A1, COL5A2, and COL1A1 gene.')
        variables[4] = variables[4] + 1

    if age <  16 and variables[0] >= 0.66 and variables[8] >= 2 and variables[9] == 1 or age >=  16 and age < 50 and variables[0] >= 0.55 and variables[8] >= 2 and variables[9] == 1 or age >= 50 and variables[0] >= 0.44 and variables[8] >= 2 and variables[9] == 1:
        print('Based on your answers, the patient meets the minimal clinical criteria for Classical-like Ehlers-Danlos Syndrome. We recommend gene specific testing specifically targeted at the TNXB gene.')
        variables[7] = variables[7] + 1

    if age <  16 and variables[0] >= 0.66 and variables[11] == 2 or age >=  16 and age < 50 and variables[0] >= 0.55 and variables[11] == 2 or age >= 50 and variables[0] >= 0.44 and variables[11] == 2 or variables[11] == 2 and variables[12] >= 1 or variables[11] == 2 and variables[13] >= 1.5:
        print('Based on your answers, the patient meets the minimal clinical criteria for Cardiac valvular Ehlers-Danlos Syndrome. We recommend gene specific testing specifically targeted at the COL1A2 gene.')
        variables[10] = variables[10] + 1

    if variables[15] >= 1 or variables[16] >= 5.99 or variables[0] >= 0.44  and variables[16] >= 4.99:
        print('Based on your answers, the patient meets the minimal clinical criteria for Vascular Ehlers-Danlos Syndrome. We recommend gene specific testing specifically targeted at the COL3A1 and COL1A1 gene.')
        variables[14] = variables[14] + 1

    if age <  16 and variables[0] >= 0.66 and variables[22] == 1 and variables[23] == 1 and variables[25] >= 2 or age >=  16 and age < 50 and variables[0] >= 0.55 and variables[22] == 1 and variables[23] == 1 and variables[25] >= 2 or age >= 50 and variables[0] >= 0.44 and variables[22] == 1 and variables[23] == 1 and variables[25] >= 2 or variables[22] == 1 and variables[24] == 1:
        print('Based on your answers, the patient meets the minimal clinical criteria for Arthrochalasia Ehlers-Danlos Syndrome. We recommend gene specific testing specifically targeted at the COL1A1 and COL1A2 gene.')
        variables[21] = variables[21] + 1

    if age <  16 and variables[0] >= 0.66 and variables[27] >= 1.66 and variables[29] >= 2 or age >=  16 and age < 50 and variables[0] >= 0.55 and variables[27] >= 1.66 and variables[29] >= 2 or age >= 50 and variables[0] >= 0.44 and variables[27] >= 1.66 and variables[29] >= 2 or variables[27] >= 1.66 and variables[28] >= 1 or variables[27] >= 1.66 and variables[29] >= 3:
        print('Based on your answers, the patient meets the minimal clinical criteria for Dermatosparaxis Ehlers-Danlos Syndrome. We recommend gene specific testing specifically targeted at the ADAMTS2 gene.')
        variables[26] = variables[26] + 1

    if age <  16 and variables[0] >= 0.66 and variables[31] == 2 and variables[32] == 1 or age >=  16 and age < 50 and variables[0] >= 0.55 and variables[31] == 2 and variables[32] == 1 or age >= 50 and variables[0] >= 0.44 and variables[31] == 2 and variables[32] == 1 or variables[31] == 2 and variables[33] >= 2.66:
        print('Based on your answers, the patient meets the minimal clinical criteria for Kyphoscoliotic Ehlers-Danlos Syndrome. We recommend gene specific testing specifically targeted at the PLOD1 and FKBP14 gene.')
        variables[30] = variables[30] + 1

    if variables[35] == 1 and variables[36] >= 1 or variables[35] == 1 and variables[37] >= 3:
        print('Based on your answers, the patient meets the minimal clinical criteria for Brittle Cornea Syndrome. We recommend gene specific testing specifically targeted at the ZNF469 and PRDM5 gene.')
        variables[34] = variables[34] + 1

    if variables[39] >= 1 and age < 10 and variables[40] >= 0.66 or variables[39] >= 1 and age >= 10 and variables[40] >= 1:
        print('Based on your answers, the patient meets the minimal clinical criteria for Musculocontractural Ehlers-Danlos Syndrome. We recommend gene specific testing specifically targeted at the CHST14 and DSE gene.')
        variables[38] = variables[38] + 1

    if variables[42] >= 1 and variables[43] == 1 or variables[42] >= 1 and variables[45] >= 0.44 or variables[42] >= 1 and variables[44] >= 3:
        print('Based on your answers, the patient meets the minimal clinical criteria for Myopathic Ehlers-Danlos Syndrome. We recommend gene specific testing specifically targeted at the COL12A1 gene.')
        variables[41] = variables[41] + 1

    if variables[47] == 1 and variables[48] >= 2 and variables[49] >= 0.4 or variables[47] == 2 and variables[48] >= 1 and variables[49] >= 0.4 or variables[0] >= 0.44 and variables[47] == 2 and variables[48] >= 1 or variables[0] >= 0.44 and variables[47] == 1 and variables[48] >= 2:
        print('Based on your answers, the patient meets the minimal clinical criteria for Periodontal Ehlers-Danlos Syndrome. We recommend gene specific testing specifically targeted at the C1R and C1S gene.')
        variables[46] = variables[46] + 1

    if variables[51] == 2 and variables[52] >= 2 and variables[53] >= 2.4:
        print('Based on your answers, the patient meets the minimal clinical criteria for Spondylodysplastic Ehlers-Danlos Syndrome. We recommend gene specific testing specifically targeted at the B4GALT7, B3GALT6, and SLC9A13 gene.')
        variables[50] = variables[50] + 1

    if variables[66] == 4:
        print('Based on your answers, the patient meets the minimal clinical criteria for Loeys-Dietz Syndrome. We recommend gene specific testing specifically targeted at the TGFBR1, TGFBR2, SMAD3, and TGFB2 gene.')
        variables[65] = variables[65] + 1

    # Marfan family or history side:
    if variables[68] >= 6.6 and variables[72] == 1 or variables[68] >= 6.6 and variables[69] == 1 or variables[72] == 1 and variables[71] == 1 or variables[71] == 1 and variables[69] == 1 or variables[72] == 1 and variables[69] == 1:
        print("Based on your answers, the patient meets the criteria for Marfan Syndrome. Though a genetic test is not mandatory in this case, it may be helpful to pursue gene specific testing on the FBN1 gene so that the patient's family members are able to assess their risk of having Marfan Sydrome.")
        marfan = marfan + 1
    if variables[72] == 1 and variables[70] == 1 or variables[71] == 1 and variables[70] == 1:
        print('Based on your answers, the patient meets the criteria for Marfan Syndrome. As the patient has already underwent gentic testing, we recommend following up with a physician about possible treatments and how to monitor this condition.')
        variables[67] = variables[67] + 1

    # Hypermobile EDS
    if age <  16 and variables[0] >= 0.66 and variables[18] >= 5 and variables[19] == 1 and variables[4] == 0 and variables[7] == 0 and variables[10] == 0 and variables[14] == 0 and variables[21] == 0 and variables[26] == 0 and variables[30] == 0 and variables[34] == 0 and variables[38] == 0 and variables[41] == 0 and variables[46] == 0 and variables[50] == 0 and variables[65] == 0 and variables[67] == 0 or age >=  16 and age < 50 and variables[0] >= 0.55 and variables[18] >= 5 and variables[19] == 1 and variables[4] == 0 and variables[7] == 0 and variables[10] == 0 and variables[14] == 0 and variables[21] == 0 and variables[26] == 0 and variables[30] == 0 and variables[34] == 0 and variables[38] == 0 and variables[41] == 0 and variables[46] == 0 and variables[50] == 0 and variables[65] == 0 and variables[67] == 0 or age >= 50 and variables[0] >= 0.44 and variables[18] >= 5 and variables[19] == 1 and variables[4] == 0 and variables[7] == 0 and variables[10] == 0 and variables[14] == 0 and variables[21] == 0 and variables[26] == 0 and variables[30] == 0 and variables[34] == 0 and variables[38] == 0 and variables[41] == 0 and variables[46] == 0 and variables[50] == 0 and variables[65] == 0 and variables[67] == 0 or age <  16 and variables[0] >= 0.66 and variables[18] >= 5 and variables[20] >= 1 and variables[4] == 0 and variables[7] == 0 and variables[10] == 0 and variables[14] == 0 and variables[21] == 0 and variables[26] == 0 and variables[30] == 0 and variables[34] == 0 and variables[38] == 0 and variables[41] == 0 and variables[46] == 0 and variables[50] == 0 and variables[65] == 0 and variables[67] == 0 or age >=  16 and age < 50 and variables[0] >= 0.55 and variables[18] >= 5 and variables[20] >= 1 and variables[4] == 0 and variables[7] == 0 and variables[10] == 0 and variables[14] == 0 and variables[21] == 0 and variables[26] == 0 and variables[30] == 0 and variables[34] == 0 and variables[38] == 0 and variables[41] == 0 and variables[46] == 0 and variables[50] == 0 and variables[65] == 0 and variables[67] == 0 or age >= 50 and variables[0] >= 0.44 and variables[18] >= 5 and variables[20] >= 1 and variables[4] == 0 and variables[7] == 0 and variables[10] == 0 and variables[14] == 0 and variables[21] == 0 and variables[26] == 0 and variables[30] == 0 and variables[34] == 0 and variables[38] == 0 and variables[41] == 0 and variables[46] == 0 and variables[50] == 0 and variables[65] == 0 and variables[67] == 0 or age <  16 and variables[0] >= 0.66 and variables[20] >= 1 and variables[19] == 1 and variables[4] == 0 and variables[7] == 0 and variables[10] == 0 and variables[14] == 0 and variables[21] == 0 and variables[26] == 0 and variables[30] == 0 and variables[34] == 0 and variables[38] == 0 and variables[41] == 0 and variables[46] == 0 and variables[50] == 0 and variables[65] == 0 and variables[67] == 0 or age >=  16 and age < 50 and variables[0] >= 0.55 and variables[20] >= 1 and variables[19] == 1 and variables[4] == 0 and variables[7] == 0 and variables[10] == 0 and variables[14] == 0 and variables[21] == 0 and variables[26] == 0 and variables[30] == 0 and variables[34] == 0 and variables[38] == 0 and variables[41] == 0 and variables[46] == 0 and variables[50] == 0 and variables[65] == 0 and variables[67] == 0 or age >= 50 and variables[0] >= 0.44 and variables[20] >= 1 and variables[19] == 1 and variables[4] == 0 and variables[7] == 0 and variables[10] == 0 and variables[14] == 0 and variables[21] == 0 and variables[26] == 0 and variables[30] == 0 and variables[34] == 0 and variables[38] == 0 and variables[41] == 0 and variables[46] == 0 and variables[50] == 0 and variables[65] == 0 and variables[67] == 0:
        print('Based on your answers, the patient meets the minimal clinical criteria for Hypermobile Ehlers-Danlos Syndrome. There is currently no genetic test for this HCTD so we recommend following up with a doctor about this possible diagnosis for more information about treatment and concerns.')
        variables[17] = variables[17] + 1
        
    # Hypermobility Spectrum Disorders
    if age <  16 and variables[0] >= 0.66 and variables[58] >= 1 and variables[4] == 0 and variables[7] == 0 and variables[10] == 0 and variables[14] == 0 and variables[17] == 0 and variables[21] == 0 and variables[26] == 0 and variables[30] == 0 and variables[34] == 0 and variables[38] == 0 and variables[41] == 0 and variables[46] == 0 and variables[50] == 0 and variables[65] == 0 and variables[67] == 0 or age >=  16 and age < 50 and variables[0] >= 0.55 and variables[58] >= 1 and variables[4] == 0 and variables[7] == 0 and variables[10] == 0 and variables[14] == 0 and variables[17] == 0 and variables[21] == 0 and variables[26] == 0 and variables[30] == 0 and variables[34] == 0 and variables[38] == 0 and variables[41] == 0 and variables[46] == 0 and variables[50] == 0 and variables[65] == 0 and variables[67] == 0 or age >= 50 and variables[0] >= 0.44 and variables[58] >= 1 and variables[17] == 0 and variables[4] == 0 and variables[7] == 0 and variables[10] == 0 and variables[14] == 0 and variables[17] == 0 and variables[21] == 0 and variables[26] == 0 and variables[30] == 0 and variables[34] == 0 and variables[38] == 0 and variables[41] == 0 and variables[46] == 0 and variables[50] == 0 and variables[65] == 0 and variables[67] == 0:
        print("Based on your answers, the patient meets the minimal clinical criteria for Generalized Hypermobility Spectrum Disorder. We do not recommend pursuing genetic testing unless new concerns/symptoms appear that suggest a different HCTD. We do recommend following up with a doctor about the patient's musculoskeletal symptoms.")
        variables[57] = variables[57] + 1

    if age <  16 and variables[0] >= 0.66 and variables[57] == 0 and variables[4] == 0 and variables[7] == 0 and variables[10] == 0 and variables[14] == 0 and variables[17] == 0 and variables[21] == 0 and variables[26] == 0 and variables[30] == 0 and variables[34] == 0 and variables[38] == 0 and variables[41] == 0 and variables[46] == 0 and variables[50] == 0 and variables[65] == 0 and variables[67] == 0 or age >=  16 and age < 50 and variables[0] >= 0.55 and variables[57] == 0 and variables[4] == 0 and variables[7] == 0 and variables[10] == 0 and variables[14] == 0 and variables[17] == 0 and variables[21] == 0 and variables[26] == 0 and variables[30] == 0 and variables[34] == 0 and variables[38] == 0 and variables[41] == 0 and variables[46] == 0 and variables[50] == 0 and variables[65] == 0 and variables[67] == 0 or age >= 50 and variables[0] >= 0.44 and variables[57] == 0 and variables[4] == 0 and variables[7] == 0 and variables[10] == 0 and variables[14] == 0 and variables[17] == 0 and variables[21] == 0 and variables[26] == 0 and variables[30] == 0 and variables[34] == 0 and variables[38] == 0 and variables[41] == 0 and variables[46] == 0 and variables[50] == 0 and variables[65] == 0 and variables[67] == 0:
        print('Based on your answers, the patient meets the minimal clinical criteria for Asymptomatic General Joint Hypermobility. We do not recommend pursuing genetic testing or follow up care unless new concerns/symptoms appear that suggest a different HCTD.')
        variables[54] = variables[54] + 1

    if variables[2] >= 0.22 and variables[62] >= 1 and variables[57] == 0 and variables[54] == 0 and variables[4] == 0 and variables[7] == 0 and variables[10] == 0 and variables[14] == 0 and variables[17] == 0 and variables[21] == 0 and variables[26] == 0 and variables[30] == 0 and variables[34] == 0 and variables[38] == 0 and variables[41] == 0 and variables[46] == 0 and variables[50] == 0 and variables[65] == 0 and variables[67] == 0:
        print("Based on your answers, the patient meets the minimal clinical criteria for Peripheral Hypermobility Spectrum Disorder. We do not recommend pursuing genetic testing unless new concerns/symptoms appear that suggest a different HCTD. We do not recommend pursuing genetic testing unless new concerns/symptoms appear that suggest a different HCTD. We do recommend following up with a doctor about the patient's musculoskeletal symptoms.")
        variables[61] = variables[61] + 1

    if variables[2] >= 0.22 and variables[61] == 0 and variables[54] == 0 and variables[4] == 0 and variables[57] == 0 and variables[7] == 0 and variables[10] == 0 and variables[14] == 0 and variables[17] == 0 and variables[21] == 0 and variables[26] == 0 and variables[30] == 0 and variables[34] == 0 and variables[38] == 0 and variables[41] == 0 and variables[46] == 0 and variables[50] == 0 and variables[65] == 0 and variables[67] == 0:
        print('Based on your answers, the patient meets the minimal clinical criteria for Asymptomatic Peripheral Joint Hypermobility. We do not recommend pursuing genetic testing or follow up care unless new concerns/symptoms appear that suggest a different HCTD.')
        variables[56] = variables[56] + 1

    if variables[3] >= 0.40 and variables[64] >= 1 and variables[61] == 0 and variables[57] == 0 and variables[4] == 0 and variables[7] == 0 and variables[10] == 0 and variables[14] == 0 and variables[17] == 0 and variables[21] == 0 and variables[26] == 0 and variables[30] == 0 and variables[34] == 0 and variables[38] == 0 and variables[41] == 0 and variables[46] == 0 and variables[50] == 0 and variables[65] == 0 and variables[67] == 0:
        print("Based on your answers, the patient meets the minimal clinical criteria for Historical Hypermobility Spectrum Disorder. We do not recommend pursuing genetic testing unless new concerns/symptoms appear that suggest a different HCTD. We do not recommend pursuing genetic testing unless new concerns/symptoms appear that suggest a different HCTD. We do recommend following up with a doctor about the patient's musculoskeletal symptoms.")
        variables[63] = variables[63] + 1

    if variables[1] >= 0.11 and variables[1] < 0.22 and variables[60] >= 1 and variables[57] == 0 and variables[61] == 0 and variables[3] == 0 and variables[4] == 0 and variables[7] == 0 and variables[10] == 0 and variables[14] == 0 and variables[17] == 0 and variables[21] == 0 and variables[26] == 0 and variables[30] == 0 and variables[34] == 0 and variables[38] == 0 and variables[41] == 0 and variables[46] == 0 and variables[50] == 0 and variables[65] == 0 and variables[67] == 0:
        print("Based on your answers, the patient meets the minimal clinical criteria for Localized Hypermobility Spectrum Disorder. We do not recommend pursuing genetic testing unless new concerns/symptoms appear that suggest a different HCTD. We do not recommend pursuing genetic testing unless new concerns/symptoms appear that suggest a different HCTD. We do recommend following up with a doctor about the patient's musculoskeletal symptoms.")
        variables[59] = variables[59] + 1
        
    if variables[1] >= 0.11 and variables[1] < 0.22 and variables[59] == 0 and variables[54] == 0 and variables[57] == 0 and variables[3] == 0 and variables[56] == 0 and variables[4] == 0 and variables[7] == 0 and variables[10] == 0 and variables[14] == 0 and variables[17] == 0 and variables[21] == 0 and variables[26] == 0 and variables[30] == 0 and variables[34] == 0 and variables[38] == 0 and variables[41] == 0 and variables[46] == 0 and variables[50] == 0 and variables[65] == 0 and variables[67] == 0:
        print('Based on your answers, the patient meets the minimal clinical criteria for Asymptomatic Localized Joint Hypermobility. We do not recommend pursuing genetic testing or follow up care unless new concerns/symptoms appear that suggest a different HCTD.')
        variables[55] = variables[55] + 1

    # No diagnosis
    if variables[4] == 0 and variables[7] == 0 and variables[10] == 0 and variables[14] == 0 and variables[17] == 0 and variables[21] == 0 and variables[26] == 0 and variables[30] == 0 and variables[34] == 0 and variables[38] == 0 and variables[41] == 0 and variables[46] == 0 and variables[50] == 0 and variables[65] == 0 and variables[67] == 0 and variables[54] == 0 and variables[55] == 0 and variables[56] == 0 and variables[57] == 0 and variables[59] == 0 and variables[61] == 0 and variables[63] == 0:
        print('Based on your answers, it does not appear that the patient possesses one of the HCTDs we screen for. There is still a possibility that the patient has a HCTD that is not screened for during this program.')


# In[ ]:


if __name__ == "__main__":
    intro()
    age, sex = get_patient_info() 
    variables = {}
    for i in range(73):
        variables[i] = 0
    questions_dict = get_questions("Dots_Questions.txt")
    systems = get_systems()
    variables = get_symptoms("Variable_Information.txt", questions_dict, systems)
    requirements(variables, age)

