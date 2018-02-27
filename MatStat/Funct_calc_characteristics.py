from scipy.stats import t, norm
import numpy as np
import math


class CyslChar(object):
    def mean_data(self, dist):  # Середнє значення вибірки
        sum = 0
        for i in dist:
            sum += i
        return sum / np.shape(dist)[0]

    def med(self, dist):  # Медіана вибірки
        return np.median(dist)

    def med_Uol(self, dist):  # Медіана Уолша
        sum = []
        for i in range(np.shape(dist)[0]):
            for j in range(i+1, np.shape(dist)[0]):
                sum.append((dist[i] + dist[j])/2)
        return self.med(sum)

    def mad(self, med):  # Медіана абсолютних відхилень від медіани
        return 1.483*med

    def med_mean(self, dist, alpha):  # Усічене середнє
        k = int(alpha*len(dist))
        sum = 0
        for i in range(k+1, len(dist)-k):
            sum += dist[i]
        return sum/(np.shape(dist)[0]-2*k)

    def disp_z(self, dist, mean_dist):  # Зсунена дисперсія
        sum = []
        for i in dist:
            sum.append(pow(i, 2) - pow(mean_dist, 2))
        return np.sum(sum) / np.shape(dist)[0]

    def disp(self, dist, mean_dist):  # Незсунена дисперсія
        sum = []
        for i in dist:
            sum.append(pow(i-mean_dist, 2))
        return np.sum(sum) / ((np.shape(dist)[0]) - 1)

    def coef_asim(self, dist, disp_z, mean_dist):  # Коефіцієнт асиметрії
        sum = []
        for i in dist:
            sum.append(pow((i-mean_dist), 3))
        return np.sum(sum) / (np.shape(dist)[0]*(pow(disp_z, 3)))

    def coef_asim_zcun(self, lendis, coef_asim):  # Коефіцієнт асиметрії зсунений
        return (np.sqrt(lendis*(lendis-1))) / ((lendis-2)*coef_asim)

    def coef_ecsces_z(self, sigma_z, dist, mean):  # Коефіцієнт ексцесу, зсунений
        sum = []
        for i in dist:
            sum.append(pow((i-mean), 4))
        return np.sum(sum) / (np.shape(dist)[0])*pow(sigma_z, 4)

    def coef_ecsces(self, coef_ecs_z, lendist):  # Коефіцієнт ексцесу, незсунений
        return ((math.pow(lendist, 2) - 1) / (lendist-2)*(lendist-3))*((coef_ecs_z-3) + 6/(lendist+1))

    def coef_cont_ecses(self, coef_ecs):  # Коефіцієнт контрексцесу
        return 1/math.sqrt(abs(coef_ecs))

    def coef_var_Pirsona(self, sigma, mean, mad, med):  # Коефіцієнт варіації Пірсона
        if mean > 0.01:
            return sigma / mean
        else:
            return mad / med

    def max_data(self, dist):  # Максимум вибірки
        return np.max(dist)

    def min_data(self, dist):  # Мінімум вибірки
        return np.min(dist)

    def mean_confidence_interval_lower(self, mean, sigma, lendist):  # Нижня оцінка середнього
        se = sigma / math.sqrt(lendist)
        if lendist >= 60:
            t_critical = t.ppf(q=0.975, df=lendist - 1)
        else:
            t_critical = abs(norm.ppf(0.025))
        m_low = mean - t_critical * se

        return m_low

    def mean_confidence_interval_upper(self, mean, sigma, lendist):  # Верхня оцінка середнього
        se = sigma / math.sqrt(lendist)
        if lendist >= 60:
            t_critical = t.ppf(q=0.975, df=lendist - 1)
        else:
            t_critical = abs(norm.ppf(0.025))
        m_u = mean + t_critical * se

        return m_u

    def return_sigma_mean_lower(self, mean, sigma, lendist):  # Нижня оцінка сер. квад. відхилення
        se = sigma / math.sqrt(lendist*2)
        if lendist >= 60:
            t_critical = t.ppf(q=0.975, df=lendist - 1)
        else:
            t_critical = abs(norm.ppf(0.025))
        sig_low = mean - t_critical * se

        return sig_low

    def return_sigma_mean_upper(self, mean, sigma, lendist):  # Верхня оцінка сер. квад. відхилення
        se = sigma / math.sqrt(lendist*2)
        if lendist >= 60:
            t_critical = t.ppf(q=0.975, df=lendist - 1)
        else:
            t_critical = abs(norm.ppf(0.025))
        sig_u = mean + t_critical * se

        return sig_u
