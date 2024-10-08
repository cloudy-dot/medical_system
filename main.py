import tkinter
from tkinter import simpledialog, messagebox
import secrets
import hashlib


###################################################################################################
class Login:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("MCMS - LOGIN")

        self.usernameLabel = tkinter.Label(self.window, text="Username")
        self.usernameEntry = tkinter.Entry(self.window, width=25)

        self.passwordLabel = tkinter.Label(self.window, text="Password")
        self.passwordEntry = tkinter.Entry(self.window, width=25)
        self.passwordEntry = tkinter.Entry(self.window, width=25, show='*') 

        self.loginButton = tkinter.Button(self.window, text="Login", command=self.login)

        self.window.geometry("600x700")

        self.usernameLabel.pack(side="top")
        self.usernameEntry.pack(side="top")
        self.passwordLabel.pack(side="top")
        self.passwordEntry.pack(side="top")
        self.loginButton.pack(side="top", pady=10)
        tkinter.mainloop()

    def login(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get().strip()


        if username == "superadmin" and password == "superadmin":
          self.window.destroy()
          SuperAdmin()
        elif self.checkCredentials(username, password, "admins.txt"):
          self.window.destroy()
          Admin(username)
        elif self.checkCredentials(username, password, "doctors.txt"):
          self.window.destroy()
          Doctor(username)
        else:
            messagebox.showerror("Error", "Invalid username or password")


    def checkCredentials(self, username, password, filePath):
      with open(filePath, "r") as file:
        for line in file:
            data = line.strip().split(",")
  
            if filePath == "admins.txt":
              storedUsername = data[0]
              storedHashedPassword = data[2]
            elif filePath == "doctors.txt":
              storedUsername = data[0]
              storedHashedPassword = data[3]
            else:
                continue
  
            if username == storedUsername and hashlib.sha256(password.encode('utf-8')).hexdigest() == storedHashedPassword:
                return True
      return False
      
###################################################################################################

class SuperAdmin:
  def __init__(self):
    self.window = tkinter.Tk()
    self.window.title("MCMS - SUPERADMIN")

    self.registerAdminButton = tkinter.Button(self.window, text="Register Admin", command=self.registerAdmin)
    self.registerDoctorButton = tkinter.Button(self.window, text="Register Doctor", command=self.registerDoctor)
    self.logoutButton = tkinter.Button(self.window, text="Log Out", command=self.logout)

    self.window.geometry("600x700")

    self.registerAdminButton.pack(side="top", pady=10)
    self.registerDoctorButton.pack(side="top", pady=10)
    self.logoutButton.pack(side="top", pady=10)


  def registerAdmin(self):
        while True:
            adminUser = simpledialog.askstring("Input", "Enter admin username:")
            if adminUser is None:
                return
            if ' ' in adminUser:
                messagebox.showerror("Error", "Spaces are not allowed in the username. Please try again.")
            else:
                break

        adminAddress = simpledialog.askstring("Input", "Enter admin address:")
        if adminAddress is None:
            return

        adminPassword = simpledialog.askstring("Input", "Enter admin password:")
        if adminPassword is None:
            return

        encryptedPassword = hashlib.sha256(adminPassword.encode('utf-8')).hexdigest()

        with open("admins.txt", "a") as adminFile:
            adminFile.write(adminUser + "," + adminAddress + "," + encryptedPassword + "\n")
        
        messagebox.showinfo("Registration Successful", "Admin registered successfully")

  def registerDoctor(self):
        while True:
            doctorUser = simpledialog.askstring("Input", "Enter doctor username:")
            if doctorUser is None:
                return
            if ' ' in doctorUser:
                messagebox.showerror("Error", "Spaces are not allowed in the username. Please try again.")
            else:
                break

        doctorJob = simpledialog.askstring("Input", "Enter doctor job:")
        if doctorJob is None:
            return
        doctorAddress = simpledialog.askstring("Input", "Enter doctor address:")
        if doctorAddress is None:
            return

        doctorPassword = simpledialog.askstring("Input", "Enter doctor password:")
        if doctorPassword is None:
            return

        encryptedPassword = hashlib.sha256(doctorPassword.encode('utf-8')).hexdigest()

        with open("doctors.txt", "a") as doctorFile:
            doctorFile.write(doctorUser + "," + doctorJob + "," + doctorAddress + "," + encryptedPassword + "\n")
        
        messagebox.showinfo("Registration Successful", "Doctor registered successfully")

  def logout(self):
    self.window.destroy()
    Login()

###################################################################################################

class Admin:
  def __init__(self, adminUsername):
    self.window = tkinter.Tk()
    self.window.title("MCMS - ADMIN")
    self.adminUsername = adminUsername
    
    self.viewDoctorButton = tkinter.Button(self.window, text="View Doctors", command=self.viewDoctor)
    self.updateDoctorButton = tkinter.Button(self.window, text="Update Doctor", command=self.updateDoctor)
    self.deleteDoctorButton = tkinter.Button(self.window, text="Delete Doctor", command=self.deleteDoctor)
    self.enrollPatientButton = tkinter.Button(self.window, text="Enroll Patient", command=self.enrollPatient)
    self.bookAppointmentButton = tkinter.Button(self.window, text="Book Appointment", command=self.bookAppointment)
    self.assignButton = tkinter.Button(self.window, text="Assign Patient", command=self.assignPatient)
    self.viewPatientRecordButton = tkinter.Button(self.window, text="Patient Record", command=self.patientRecord)
    self.openExtendedAdminButton = tkinter.Button(self.window, text="Open Extended Admin", command=self.openExtendedAdmin)
    self.logoutButton = tkinter.Button(self.window, text="Log Out", command=self.logout)

    self.window.geometry("600x700")
    
    self.viewDoctorButton.pack(side = "top", pady = 10)
    self.updateDoctorButton.pack(side = "top", pady = 10)
    self.deleteDoctorButton.pack(side = "top", pady = 10)
    self.enrollPatientButton.pack(side = "top", pady = 10)
    self.bookAppointmentButton.pack(side = "top", pady = 10)
    self.assignButton.pack(side = "top", pady = 10)
    self.viewPatientRecordButton.pack(side = "top", pady = 10)
    self.openExtendedAdminButton.pack(side = "top", pady = 10)
    self.logoutButton.pack(side = "top", pady = 10)

  def viewDoctor(self):
    doctorUser = simpledialog.askstring("Input", "Enter doctor username:")

    with open("doctors.txt", "r") as doctorFile:
        doctorFound = False
        for line in doctorFile:
            doctorData = line.strip().split(",")
            if doctorData[0] == doctorUser:
                messagebox.showinfo("Doctor data", "Name: {0}\nJob: {1}\nAddress: {2}".format(doctorData[0], doctorData[1], doctorData[2]))
                doctorFound = True
                break

        if doctorFound == False:
            messagebox.showerror("Doctor Not Found", "Doctor {0} not found in the list.".format(doctorUser))


  def updateDoctor(self):
    doctorUser = simpledialog.askstring("Input", "Enter doctor username:")
    if doctorUser is None: 
        return

    found = False

    with open("doctors.txt", "r") as doctorFile:
        lines = doctorFile.readlines()

    with open("doctors.txt", "w") as doctorFile:
        for line in lines:
            doctorData = line.strip().split(",")
            if doctorData[0] == doctorUser:
                found = True
                choice = simpledialog.askstring("Input", "Change name, job or address?")
                if choice == "name":
                    newName = simpledialog.askstring("Input", "Enter new name:")
                    if newName is not None:
                        doctorData[0] = newName
                elif choice== "job":
                    newJob = simpledialog.askstring("Input", "Enter new job:")
                    if newJob is not None:
                        doctorData[1] = newJob
                elif choice == "address":
                    newAddress = simpledialog.askstring("Input", "Enter new address:")
                    if newAddress is not None:
                        doctorData[2] = newAddress

                doctorFile.write(",".join(doctorData) + "\n")
            else:
                doctorFile.write(line)

    if not found:
        messagebox.showerror("Doctor Not Found", "Doctor {0} not found in the file.".format(doctorUser))
    else:
        messagebox.showinfo("Update Successful", "Doctor {0} updated successfully.".format(doctorUser))


  def deleteDoctor(self):
    i = 0
    found = False
    
    doctorUser = simpledialog.askstring("Input", "Enter doctor username:")
    with open("doctors.txt", "r") as doctorFile:
      lines = doctorFile.readlines()
      
    for line in lines:
      i = i+1
      doctorData = line.strip().split(",")
      if doctorData[0] == doctorUser:
        del lines[i - 1]
        found = True
    
    with open("doctors.txt", "w") as doctorFile:
        doctorFile.writelines(lines)

    if found == True:
      messagebox.showinfo("Update Successful", "Doctor {0} deleted successfully.".format(doctorUser))
    else:
      messagebox.showerror("Doctor Not Found", "Doctor {0} not found in the file.".format(doctorUser))

      
  def enrollPatient(self):
    patientName = simpledialog.askstring("Input", "Enter patient name:")
    if patientName is None: 
        return
    patientAddress = simpledialog.askstring("Input", "Enter patient address:")
    if patientAddress is None:
        return

    temp = "null"

    with open("patients.txt", "a") as patientFile:
        patientFile.write(patientName + "," + patientAddress + "," + temp + "," + temp + "," + temp + "," + temp + "\n")
        messagebox.showinfo("Registration Successful", "Patient registered successfully")

    
  def bookAppointment(self):
    patient = simpledialog.askstring("Input", "Enter patient name:")
    if patient is None: 
        return

    found = False

    with open("patients.txt", "r") as patientFile:
        lines = patientFile.readlines()

    with open("patients.txt", "w") as patientFile:
        for line in lines:
            patientData = line.strip().split(",")
            if patientData[0] == patient:
                found = True
                date = simpledialog.askstring("Input", "Enter date in form yyyy-mm-dd")
                illness = simpledialog.askstring("Input", "Enter illness")
                status = "pending"

                date = date if date is not None else "null"
                illness = illness if illness is not None else "null"

                patientData[3] = date
                patientData[4] = illness
                patientData[5] = status

                patientFile.write(",".join(patientData) + "\n")
            else:
                patientFile.write(line)

    if not found:
        messagebox.showerror("Patient Not Found", "Patient {0} not found in the file.".format(patient))
    else:
        messagebox.showinfo("Update Successful", "Patient {0} updated successfully.".format(patient))


  
  def assignPatient(self):
    patient = simpledialog.askstring("Input", "Enter patient name:")
    patientFound = False

    with open("patients.txt", "r") as patientFile:
        lines = patientFile.readlines()

    with open("patients.txt", "w") as patientFile:
        for line in lines:
            patientData = line.strip().split(",")
            if patientData[0] == patient:
                doctor = simpledialog.askstring("Input", "Enter doctor name:")
                doctorFound = False

                with open("doctors.txt", "r") as doctorFile:
                    doctorLines = doctorFile.readlines()

                for doctorLine in doctorLines:
                    doctorData = doctorLine.strip().split(",")
                    if doctorData[0] == doctor:
                        doctorFound = True
                      
                        patientData[2] = doctor
                        patientData[5] = "Approved"

                if doctorFound == False:
                    messagebox.showerror("Doctor Not Found", "Doctor {0} not found in the file.".format(doctor))

                patientFound = True

            patientFile.write(",".join(patientData) + "\n")

    if patientFound == False:
        messagebox.showerror("Patient Not Found", "Patient {0} not found in the file.".format(patient))
    else:
        messagebox.showinfo("Update Successful", "Patient {0} updated successfully.".format(patient))

  

  def patientRecord(self):
    patient = simpledialog.askstring("Input", "Enter patient name:")

    patientFound = False

    with open("patients.txt", "r") as patientFile:
      lines = patientFile.readlines()

    with open("patients.txt", "w") as patientFile:
      for line in lines:
        patientData = line.strip().split(",")
        if patientData[0] == patient:
          patientFound = True
          messagebox.showinfo("Patient Record", "Patient Name: {0}\nPatient Address: {1}\nDoctor Name: {2}\nAppointment Date: {3}\nIllness: {4}\nStatus: {5}".format(patientData[0], patientData[1], patientData[2], patientData[3], patientData[4], patientData[5]))
          patientFile.write(",".join(patientData) + "\n")
        else:
          patientFile.write(line)
          

    if patientFound == False:
      messagebox.showerror("Patient Not Found", "Patient {0} not found in the file.".format(patient))

  def openExtendedAdmin(self):
    self.window.destroy() 
    ExtendedAdmin(self.adminUsername)

  def logout(self):
    self.window.destroy()
    Login()
  ##################################################################################################
class Doctor():
  def __init__(self, doctorUsername):

   self.window = tkinter.Tk()
   self.window.title("MCMS - DOCTOR")
   self.doctorUsername = doctorUsername
  
   self.viewPatientRecordButton = tkinter.Button(self.window, text="View Patient Record", command=self.patientRecord)
   self.viewAppointmentButton = tkinter.Button(self.window, text="View Appointments", command=self.viewAppointment)
   self.logoutButton = tkinter.Button(self.window, text="Log Out", command=self.logout)

   self.window.geometry("600x700")
  
   self.viewPatientRecordButton.pack(pady=10)
   self.viewAppointmentButton.pack(pady=10)
   self.logoutButton.pack(pady=10)
   tkinter.mainloop()

  def patientRecord(self):
    patient = simpledialog.askstring("Input", "Enter patient name:")

    patientFound = False

    with open("patients.txt", "r") as patientFile:
      lines = patientFile.readlines()

    with open("patients.txt", "w") as patientFile:
      for line in lines:
        patientData = line.strip().split(",")
        if patientData[0] == patient:
          patientFound = True
          messagebox.showinfo("Patient Record", "Patient Name: {0}\nPatient Address: {1}\nDoctor Name: {2}\nAppointment Date: {3}\nIllness: {4}\nStatus: {5}".format(patientData[0], patientData[1], patientData[2], patientData[3], patientData[4], patientData[5]))
          patientFile.write(",".join(patientData) + "\n")
        else:
          patientFile.write(line)


    if patientFound == False:
      messagebox.showerror("Patient Not Found", "Patient {0} not found in the file.".format(patient))

  def viewAppointment(self):
    with open("patients.txt", "r") as file:
        appointments = ""
        i = 1
        for line in file:
            patientData = line.strip().split(',')
            if patientData[2] == self.doctorUsername:
                  appointments += "Patient {0}: {1}, Appointment Date: {2}, Illness: {3}\n\n".format(i, patientData[0], patientData[3], patientData[4])
                  i += 1

        if appointments != "":
            messagebox.showinfo("Your Appointments", appointments)
        else:
            messagebox.showinfo("No Appointments", "You have no upcoming appointments.")

  def logout(self):
    self.window.destroy()
    Login()


class ExtendedAdmin():
  def __init__(self, adminUsername):
    self.window = tkinter.Tk()
    self.window.title("MCMS - ADMIN")
    self.adminUsername = adminUsername
    
    self.updateAdminButton = tkinter.Button(self.window, text="Update Admin Info", command=self.updateAdmin)
    self.dischargeButton = tkinter.Button(self.window, text="Discharge Patient", command=self.dischargePatient)
    self.viewTreatedButton = tkinter.Button(self.window, text="View Treated Patients", command=self.viewTreated)
    self.storeButton = tkinter.Button(self.window, text="Store Patient Data", command=self.storeData)
    self.loadButton = tkinter.Button(self.window, text="Load Patient Data", command=self.loadData)
    self.reportButton = tkinter.Button(self.window, text="Management Report", command=self.managementReport)
    self.backButton = tkinter.Button(self.window, text="BACK", command=self.back)

    self.window.geometry("600x700")

    self.updateAdminButton.pack(pady=10)
    self.dischargeButton.pack(pady=10)
    self.viewTreatedButton.pack(pady=10)
    self.storeButton.pack(pady=10)
    self.loadButton.pack(pady=10)
    self.reportButton.pack(pady=10)
    self.backButton.pack(pady=10)
    tkinter.mainloop()

  def dischargePatient(self):
    i = 0
    found = False
    temp = ""

    patient = simpledialog.askstring("Input", "Enter patient name:")
    with open("patients.txt", "r") as patientFile:
      lines = patientFile.readlines()

    for line in lines:
      i = i+1
      patientData = line.strip().split(",")
      if patientData[0] == patient:
        temp = lines[i-1]
        del lines[i - 1]
        found = True

    with open("patients.txt", "w") as patientFile:
      patientFile.writelines(lines)

    with open("treated_patients.txt", "a") as treatedFile:
      treatedFile.write(temp)

    if found == True:
      messagebox.showinfo("Update Successful", "Patient {0} discharged successfully.".format(patient))
    else:
      messagebox.showerror("Doctor Not Found", "Patient {0} not found in the list.".format(patient))


  def viewTreated(self):

    with open("treated_patients.txt", "r") as file:
        patients = ""
        i = 1
        for line in file:
            patientData = line.strip().split(',')
            patients += "Patient {0}: {1}, Address: {2}, Illness: {3}, Doctor: {4}, Appointment Date: {5}\n\n".format(i, patientData[0], patientData[1], patientData[4], patientData[2], patientData[3])
            i += 1

        if patients != "":
            messagebox.showinfo("Treated Patients", patients)
        else:
            messagebox.showinfo("No Patients", "There are no treated patients")

  def updateAdmin(self):
    with open("admins.txt", "r") as adminFile:
        lines = adminFile.readlines()

    with open("admins.txt", "w") as adminFile:
        for line in lines:
            adminData = line.strip().split(",")
            if adminData[0] == self.adminUsername:
                choice = simpledialog.askstring("Input", "Enter the admin info you want to update (name or address)")
                if choice is None: 
                    adminFile.write(line)
                    return

                if choice.lower() == "name":
                  newName = simpledialog.askstring("Input", "Enter the new name:")
                  if newName is not None:
                      adminData[0] = newName
                      adminFile.write(",".join(adminData) + "\n")
                      self.adminUsername = adminData[0]
                  else:
                      adminFile.write(line)
                      messagebox.showerror("Invalid Input", "Invalid input.")
                elif choice.lower() == "address":
                    newAddress = simpledialog.askstring("Input", "Enter the new address:")
                    if newAddress is not None:
                        adminData[1] = newAddress
                        adminFile.write(",".join(adminData) + "\n")
                    else:
                        adminFile.write(line)
                        messagebox.showerror("Invalid Input", "Invalid input.")
                else:
                    adminFile.write(line)
                    messagebox.showerror("Invalid Input", "Invalid input.")
            else:
                adminFile.write(line)
    

  def storeData(self, filePath="patients_data.txt"):
    with open(filePath, "w") as file:
        with open("patients.txt", "r") as patientsFile:
            file.write(patientsFile.read())
    messagebox.showinfo("Save Successful", "Patient data stored successfully.")
  
  def loadData(self, filePath="patients_data.txt"):
    patients = ""
    with open(filePath, "r") as patientsFile:
        for line in patientsFile:
            patientData = line.strip().split(',')

            patients += "Patient: {0}, Address: {1}, Illness: {2}, Doctor: {3}, Appointment Date: {4}\n\n".format( patientData[0], patientData[1], patientData[4], patientData[2], patientData[3])


    if patients != "":
        messagebox.showinfo("Patients", patients)
    else:
        messagebox.showinfo("No Patients", "There are no treated patients")

  def managementReport(self):
    totalDoctors = self.getTotalDoctors()
    patientsDoctor = self.getTotalPatientsPerDoctor()
    appointmentsMonth = self.getTotalAppointmentsPerMonthPerDoctor()
    patientsIllness = self.getTotalPatientsIllness()
    

    messagebox.showinfo("Management Report", "Total Doctors: {0}\n\nPatients per Doctor: {1}\n\nNumber of Appointments Per Doctor Per Month: {2}\n\nNumber of Patients Illness type: {3}".format(totalDoctors,patientsDoctor,appointmentsMonth,patientsIllness))
    

  def getTotalDoctors(self):
    with open("doctors.txt", "r") as doctorFile:
      lines = doctorFile.readlines()
      i = 0
      for line in lines:
        i = i+1
    return i

  def getTotalPatientsPerDoctor(self):
    patientsPerDoctor = {}
    with open("patients.txt", "r") as file:
      for line in file:
          patientData = line.strip().split(',')

          if patientData[2].lower() == 'null':
            continue
  
          if patientData[2] in patientsPerDoctor:
            patientsPerDoctor[patientData[2]] += 1
          else:
            patientsPerDoctor[patientData[2]] = 1
  
    return patientsPerDoctor


  def getTotalAppointmentsPerMonthPerDoctor(self):
    appointmentsDoctor = {}
    with open("patients.txt", "r") as file:
      for line in file:
        patientData = line.strip().split(',')

        if patientData[3].lower() == 'null':
          continue
        month = patientData[3].split('-')[1]

        if month == '01':
          monthName = 'January'
        elif month == '02':
          monthName = 'February'
        elif month == '03':
          monthName = 'March'
        elif month == '04':
          monthName = 'April'
        elif month == '05':
          monthName = 'May'
        elif month == '06':
          monthName = 'June'
        elif month == '07':
          monthName = 'July'
        elif month == '08':
          monthName = 'August'
        elif month == '09':
          monthName = 'September'
        elif month == '10':
          monthName = 'October'
        elif month == '11':
          monthName = 'November'
        elif month == '12':
          monthName = 'December'
        else:
          monthName = 'Unknown'
  
        key = "{0} : {1}".format(patientData[2], monthName)
  
        if key in appointmentsDoctor:
          appointmentsDoctor[key] += 1
        else:
          appointmentsDoctor[key] = 1
  
    return appointmentsDoctor
    

  def getTotalPatientsIllness(self):
    illnessPatient = {}
    with open("patients.txt", "r") as file:
      for line in file:
          patientData = line.strip().split(',')

          if patientData[4].lower() == 'null':
            continue
  
          if patientData[4] in illnessPatient:
            illnessPatient[patientData[4]] += 1
          else:
            illnessPatient[patientData[4]] = 1
  
    return illnessPatient

  def back(self):
    self.window.destroy()
    Admin(self.adminUsername)
  
Login()
