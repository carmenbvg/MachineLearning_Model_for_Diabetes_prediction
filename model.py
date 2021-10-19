def predict_diabetes(pregnancies=None,
                     glucose=None,
                     blood_pressure=None,
                     skinfold=None,
                     insulin=None,
                     bmi=None,
                     diabetes_pedigree=None,
                     age=None):
    """ Predictor for Diabetes from model/61670ea9e4279b24a1020e58

        Dataset created from a study of diabetes in females 21 years or older and of Pima Indian heritage. 
        Pima Indians are an interesting population to study for diabetes because they have a higher incidence of diabetes than the general U.S. population.
        Source
        Pima Indians Diabetes Data Set[*] 
        Bache, K. & Lichman, M. (2013). UCI Machine Learning Repository[*]. Irvine, CA: University of California, School of Information and Computer Science.
        
        [*]Pima Indians Diabetes Data Set: http://archive.ics.uci.edu/ml/datasets/Pima+Indians+Diabetes
        [*]UCI Machine Learning Repository: http://archive.ics.uci.edu/ml
    """
    if (glucose is None):
        return u'False'
    if (glucose > 144):
        if (glucose > 166):
            if (bmi is None):
                return u'True'
            if (bmi > 29.23):
                if (age is None):
                    return u'True'
                if (age > 25):
                    if (diabetes_pedigree is None):
                        return u'True'
                    if (diabetes_pedigree > 1.337):
                        return u'False'
                    if (diabetes_pedigree <= 1.337):
                        if (diabetes_pedigree > 0.3065):
                            if (bmi > 45.95):
                                return u'False'
                            if (bmi <= 45.95):
                                return u'True'
                        if (diabetes_pedigree <= 0.3065):
                            if (bmi > 35.3):
                                return u'True'
                            if (bmi <= 35.3):
                                if (bmi > 33.8):
                                    return u'False'
                                if (bmi <= 33.8):
                                    if (diabetes_pedigree > 0.2835):
                                        return u'False'
                                    if (diabetes_pedigree <= 0.2835):
                                        return u'True'
                if (age <= 25):
                    return u'True'
            if (bmi <= 29.23):
                if (blood_pressure is None):
                    return u'True'
                if (blood_pressure > 79):
                    return u'False'
                if (blood_pressure <= 79):
                    if (blood_pressure > 57):
                        return u'True'
                    if (blood_pressure <= 57):
                        return u'False'
        if (glucose <= 166):
            if (age is None):
                return u'True'
            if (age > 24):
                if (bmi is None):
                    return u'True'
                if (bmi > 23.175):
                    if (pregnancies is None):
                        return u'True'
                    if (pregnancies > 7):
                        if (age > 53):
                            return u'False'
                        if (age <= 53):
                            if (bmi > 39.25):
                                if (bmi > 40.75):
                                    return u'True'
                                if (bmi <= 40.75):
                                    return u'False'
                            if (bmi <= 39.25):
                                return u'True'
                    if (pregnancies <= 7):
                        if (skinfold is None):
                            return u'True'
                        if (skinfold > 21):
                            if (blood_pressure is None):
                                return u'False'
                            if (blood_pressure > 61):
                                if (diabetes_pedigree is None):
                                    return u'False'
                                if (diabetes_pedigree > 0.333):
                                    if (pregnancies > 3):
                                        if (age > 49):
                                            return u'True'
                                        if (age <= 49):
                                            if (bmi > 39.05):
                                                return u'True'
                                            if (bmi <= 39.05):
                                                return u'False'
                                    if (pregnancies <= 3):
                                        if (glucose > 163):
                                            return u'False'
                                        if (glucose <= 163):
                                            return u'True'
                                if (diabetes_pedigree <= 0.333):
                                    return u'False'
                            if (blood_pressure <= 61):
                                return u'True'
                        if (skinfold <= 21):
                            if (bmi > 30.15):
                                if (diabetes_pedigree is None):
                                    return u'True'
                                if (diabetes_pedigree > 1.5015):
                                    return u'False'
                                if (diabetes_pedigree <= 1.5015):
                                    if (diabetes_pedigree > 0.2265):
                                        return u'True'
                                    if (diabetes_pedigree <= 0.2265):
                                        if (blood_pressure is None):
                                            return u'True'
                                        if (blood_pressure > 82):
                                            return u'True'
                                        if (blood_pressure <= 82):
                                            return u'False'
                            if (bmi <= 30.15):
                                if (bmi > 29.6):
                                    return u'False'
                                if (bmi <= 29.6):
                                    if (pregnancies > 6):
                                        return u'False'
                                    if (pregnancies <= 6):
                                        return u'True'
                if (bmi <= 23.175):
                    return u'False'
            if (age <= 24):
                if (blood_pressure is None):
                    return u'False'
                if (blood_pressure > 87):
                    return u'True'
                if (blood_pressure <= 87):
                    return u'False'
    if (glucose <= 144):
        if (bmi is None):
            return u'False'
        if (bmi > 26.86986):
            if (age is None):
                return u'False'
            if (age > 30):
                if (glucose > 82):
                    if (glucose > 106):
                        if (age > 58):
                            return u'False'
                        if (age <= 58):
                            if (bmi > 45.51667):
                                return u'True'
                            if (bmi <= 45.51667):
                                if (blood_pressure is None):
                                    return u'True'
                                if (blood_pressure > 84):
                                    if (insulin is None):
                                        return u'False'
                                    if (insulin > 109):
                                        if (skinfold is None):
                                            return u'True'
                                        if (skinfold > 19):
                                            return u'True'
                                        if (skinfold <= 19):
                                            return u'False'
                                    if (insulin <= 109):
                                        if (bmi > 43.05):
                                            return u'True'
                                        if (bmi <= 43.05):
                                            return u'False'
                                if (blood_pressure <= 84):
                                    if (glucose > 119):
                                        if (age > 41):
                                            if (blood_pressure > 77):
                                                if (skinfold is None):
                                                    return u'False'
                                                if (skinfold > 13):
                                                    if (glucose > 123):
                                                        return u'True'
                                                    if (glucose <= 123):
                                                        return u'False'
                                                if (skinfold <= 13):
                                                    return u'False'
                                            if (blood_pressure <= 77):
                                                return u'True'
                                        if (age <= 41):
                                            if (insulin is None):
                                                return u'False'
                                            if (insulin > 191):
                                                return u'False'
                                            if (insulin <= 191):
                                                if (diabetes_pedigree is None):
                                                    return u'True'
                                                if (diabetes_pedigree > 0.8325):
                                                    return u'True'
                                                if (diabetes_pedigree <= 0.8325):
                                                    if (insulin > 117):
                                                        return u'False'
                                                    if (insulin <= 117):
                                                        if (diabetes_pedigree > 0.235):
                                                            if (age > 39):
                                                                return u'False'
                                                            if (age <= 39):
                                                                if (skinfold is None):
                                                                    return u'True'
                                                                if (skinfold > 10):
                                                                    return u'True'
                                                                if (skinfold <= 10):
                                                                    if (age > 38):
                                                                        return u'True'
                                                                    if (age <= 38):
                                                                        return u'False'
                                                        if (diabetes_pedigree <= 0.235):
                                                            return u'True'
                                    if (glucose <= 119):
                                        if (skinfold is None):
                                            return u'True'
                                        if (skinfold > 39):
                                            if (skinfold > 45):
                                                return u'True'
                                            if (skinfold <= 45):
                                                return u'False'
                                        if (skinfold <= 39):
                                            if (bmi > 27.85):
                                                return u'True'
                                            if (bmi <= 27.85):
                                                if (glucose > 110):
                                                    return u'True'
                                                if (glucose <= 110):
                                                    if (bmi > 27.15):
                                                        return u'False'
                                                    if (bmi <= 27.15):
                                                        return u'True'
                    if (glucose <= 106):
                        if (diabetes_pedigree is None):
                            return u'False'
                        if (diabetes_pedigree > 0.625):
                            if (insulin is None):
                                return u'True'
                            if (insulin > 33):
                                if (diabetes_pedigree > 0.944):
                                    return u'False'
                                if (diabetes_pedigree <= 0.944):
                                    if (blood_pressure is None):
                                        return u'True'
                                    if (blood_pressure > 77):
                                        return u'False'
                                    if (blood_pressure <= 77):
                                        return u'True'
                            if (insulin <= 33):
                                return u'True'
                        if (diabetes_pedigree <= 0.625):
                            if (skinfold is None):
                                return u'False'
                            if (skinfold > 36):
                                return u'False'
                            if (skinfold <= 36):
                                if (bmi > 29.65):
                                    if (diabetes_pedigree > 0.475):
                                        return u'False'
                                    if (diabetes_pedigree <= 0.475):
                                        if (insulin is None):
                                            return u'False'
                                        if (insulin > 187):
                                            return u'False'
                                        if (insulin <= 187):
                                            if (glucose > 105):
                                                return u'False'
                                            if (glucose <= 105):
                                                if (pregnancies is None):
                                                    return u'True'
                                                if (pregnancies > 11):
                                                    return u'True'
                                                if (pregnancies <= 11):
                                                    if (glucose > 92):
                                                        if (pregnancies > 5):
                                                            if (blood_pressure is None):
                                                                return u'False'
                                                            if (blood_pressure > 79):
                                                                if (diabetes_pedigree > 0.3135):
                                                                    return u'False'
                                                                if (diabetes_pedigree <= 0.3135):
                                                                    return u'True'
                                                            if (blood_pressure <= 79):
                                                                return u'False'
                                                        if (pregnancies <= 5):
                                                            return u'True'
                                                    if (glucose <= 92):
                                                        return u'False'
                                if (bmi <= 29.65):
                                    return u'False'
                if (glucose <= 82):
                    return u'False'
            if (age <= 30):
                if (glucose > 112):
                    if (pregnancies is None):
                        return u'False'
                    if (pregnancies > 5):
                        return u'True'
                    if (pregnancies <= 5):
                        if (diabetes_pedigree is None):
                            return u'False'
                        if (diabetes_pedigree > 1.1415):
                            return u'True'
                        if (diabetes_pedigree <= 1.1415):
                            if (bmi > 31.4):
                                if (glucose > 113):
                                    if (diabetes_pedigree > 0.5245):
                                        if (insulin is None):
                                            return u'False'
                                        if (insulin > 207):
                                            return u'False'
                                        if (insulin <= 207):
                                            if (diabetes_pedigree > 0.709):
                                                if (bmi > 34.1):
                                                    return u'False'
                                                if (bmi <= 34.1):
                                                    return u'True'
                                            if (diabetes_pedigree <= 0.709):
                                                if (bmi > 34.55):
                                                    return u'True'
                                                if (bmi <= 34.55):
                                                    if (bmi > 32.8):
                                                        return u'False'
                                                    if (bmi <= 32.8):
                                                        return u'True'
                                    if (diabetes_pedigree <= 0.5245):
                                        if (bmi > 49.1):
                                            return u'True'
                                        if (bmi <= 49.1):
                                            if (blood_pressure is None):
                                                return u'False'
                                            if (blood_pressure > 69):
                                                return u'False'
                                            if (blood_pressure <= 69):
                                                if (glucose > 133):
                                                    return u'True'
                                                if (glucose <= 133):
                                                    if (insulin is None):
                                                        return u'False'
                                                    if (insulin > 31):
                                                        return u'False'
                                                    if (insulin <= 31):
                                                        if (diabetes_pedigree > 0.295):
                                                            return u'False'
                                                        if (diabetes_pedigree <= 0.295):
                                                            if (bmi > 32.95):
                                                                return u'True'
                                                            if (bmi <= 32.95):
                                                                return u'False'
                                if (glucose <= 113):
                                    return u'True'
                            if (bmi <= 31.4):
                                if (skinfold is None):
                                    return u'False'
                                if (skinfold > 14):
                                    return u'False'
                                if (skinfold <= 14):
                                    if (skinfold > 11):
                                        return u'True'
                                    if (skinfold <= 11):
                                        if (age > 23):
                                            return u'False'
                                        if (age <= 23):
                                            return u'True'
                if (glucose <= 112):
                    if (skinfold is None):
                        return u'False'
                    if (skinfold > 29):
                        if (bmi > 45.05):
                            return u'True'
                        if (bmi <= 45.05):
                            if (diabetes_pedigree is None):
                                return u'False'
                            if (diabetes_pedigree > 0.47275):
                                if (bmi > 33.45):
                                    if (bmi > 38.8):
                                        return u'False'
                                    if (bmi <= 38.8):
                                        if (skinfold > 40):
                                            return u'True'
                                        if (skinfold <= 40):
                                            if (blood_pressure is None):
                                                return u'False'
                                            if (blood_pressure > 68):
                                                return u'False'
                                            if (blood_pressure <= 68):
                                                if (bmi > 36.7):
                                                    if (bmi > 37.6):
                                                        return u'True'
                                                    if (bmi <= 37.6):
                                                        return u'False'
                                                if (bmi <= 36.7):
                                                    return u'True'
                                if (bmi <= 33.45):
                                    return u'False'
                            if (diabetes_pedigree <= 0.47275):
                                if (bmi > 32.35):
                                    return u'False'
                                if (bmi <= 32.35):
                                    if (age > 24):
                                        return u'True'
                                    if (age <= 24):
                                        return u'False'
                    if (skinfold <= 29):
                        if (bmi > 32.625):
                            if (bmi > 33.05):
                                if (blood_pressure is None):
                                    return u'False'
                                if (blood_pressure > 82):
                                    if (blood_pressure > 86):
                                        return u'False'
                                    if (blood_pressure <= 86):
                                        return u'True'
                                if (blood_pressure <= 82):
                                    return u'False'
                            if (bmi <= 33.05):
                                if (bmi > 32.8):
                                    return u'True'
                                if (bmi <= 32.8):
                                    return u'False'
                        if (bmi <= 32.625):
                            return u'False'
        if (bmi <= 26.86986):
            if (glucose > 126):
                if (pregnancies is None):
                    return u'False'
                if (pregnancies > 2):
                    if (blood_pressure is None):
                        return u'False'
                    if (blood_pressure > 73):
                        return u'False'
                    if (blood_pressure <= 73):
                        if (bmi > 24.9):
                            return u'True'
                        if (bmi <= 24.9):
                            if (blood_pressure > 68):
                                return u'True'
                            if (blood_pressure <= 68):
                                return u'False'
                if (pregnancies <= 2):
                    return u'False'
            if (glucose <= 126):
                if (bmi > 26.445):
                    if (skinfold is None):
                        return u'False'
                    if (skinfold > 21):
                        if (bmi > 26.55):
                            return u'False'
                        if (bmi <= 26.55):
                            return u'True'
                    if (skinfold <= 21):
                        return u'False'
                if (bmi <= 26.445):
                    return u'False'
