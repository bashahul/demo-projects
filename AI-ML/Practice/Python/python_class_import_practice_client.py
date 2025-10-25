{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9ea08617-06e3-4324-a4cd-e5331a12b6e8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sub-fields in AI are:\n",
      "Machine Learning\n",
      "Neural Networks\n",
      "Vision\n",
      "Robotics\n",
      "Speech Processing\n",
      "Natural Language Processing\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number 100\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100 is Even number\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Your Gender Male\n",
      "Your Age 20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Not Eligible\n"
     ]
    }
   ],
   "source": [
    "from python_class_import_practice import UtilsContainer\n",
    "# Call all the functions inside the class\n",
    "\n",
    "# print all AI sub fields\n",
    "UtilsContainer.printAISubFields()\n",
    "\n",
    "# check if odd or even\n",
    "user_input_number = int(input(\"Enter a number\"))\n",
    "UtilsContainer.checkIfOddOrEven(user_input_number)\n",
    "\n",
    "# check marraige age\n",
    "user_gender = input(\"Your Gender\")\n",
    "user_age = int(input(\"Your Age\"))\n",
    "eligiblityStatus = UtilsContainer.checkMarriageAge(user_gender, user_age)\n",
    "\n",
    "print(eligiblityStatus)\n",
    "\n",
    "UtilsContainer.calculatePercentage()\n",
    "\n",
    "print(\"Find Triangle Area\")\n",
    "base = float(input(\"Enter Base\"))\n",
    "height = float(input(\"Enter Height\"))\n",
    "\n",
    "area_value = UtilsContainer.find_triangle_area(base, height)\n",
    "print(area_value)\n",
    "\n",
    "print(\"Find Perimeter\")\n",
    "side_1 = float(input(\"Side 1\"))\n",
    "side_2 = float(input(\"Side 2\"))\n",
    "side_3 = float(input(\"Side 3\"))\n",
    "perimeter = UtilsContainer.find_triangle_perimeter(side_1,side_2, side_3)\n",
    "\n",
    "print(perimeter)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a56acba7-0caf-4066-87b1-6bad9a6889fb",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
