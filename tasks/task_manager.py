import numpy as np

#Input: num_students: int, num_subjects: int
#Output: np.ndarray (boyut: [num_students, num_subjects], 0-100 arası integer değerler)
#Açıklama:
#Öğrencilerin ders puanlarını temsil eden rastgele sayılardan oluşan bir Numpy matrisi oluştur. Bu matris tüm analizlerin temelini oluşturacak.
def create_student_score_matrix(num_students: int, num_subjects: int) -> np.ndarray:
    scores_matrix = np.random.randint(0, 101, size=(num_students, num_subjects))
    
    return scores_matrix

#Input: scores: np.ndarray
#Output: 1D Numpy dizisi (her dersin ortalama puanı)
#Açıklama:
#Verilen puan matrisinde, her bir ders için tüm öğrencilerin not ortalamasını hesapla.
def calculate_mean_per_subject(scores: np.ndarray) -> np.ndarray:
    subject_means = np.mean(scores, axis=0)
    
    return subject_means

#Input: scores: np.ndarray
#Output: 1D Numpy dizisi (her öğrencinin not varyansı)
#Açıklama:
#Her öğrencinin notlarının ne kadar değişken olduğunu anlamak için varyans değerlerini hesapla. Varyans, öğrencinin farklı derslerde ne kadar tutarlı olduğunu gösterir.
def calculate_student_variance(scores: np.ndarray) -> np.ndarray:
    subject_vars = np.var(scores, axis=1)
    
    return subject_vars

#Input: scores: np.ndarray
#Output: np.ndarray (puanı %10 artırılmış, 100'ü geçmeyen yeni matris)
#Açıklama:
#Profesör Dumbledore tüm puanlara %10 büyü bonusu verilmesini istedi. Ancak puanlar 100’ü geçemez. Puanları artır ve gerektiğinde 100 ile sınırla.
def apply_magic_curve(scores: np.ndarray) -> np.ndarray:
    curved_scores = scores * 1.1
    final_scores = np.clip(curved_scores, a_min=0, a_max=100)

    return final_scores

#Input: scores: np.ndarray, threshold: float
#Output: np.ndarray (threshold üzerindeki ortalamaya sahip öğrencilerin index listesi)
#Açıklama:
#Sınıftaki başarılı öğrencileri bul. Ortalama puanı threshold değerinin üstünde olan öğrencilerin sırasını döndür.
def get_top_students(scores: np.ndarray, threshold: float) -> np.ndarray:
    student_means = np.mean(scores, axis=1)
    top_indices = np.where(student_means > threshold)[0]

    return top_indices


#Input: scores: np.ndarray
#Output: 1D Numpy dizisi (her ders için en yüksek puan)
#Açıklama:
#Hangi öğrenci hangi derste parlamış? scores matrisi için en yüksek alınan puanı belirle.
def subject_wise_max_scores(scores: np.ndarray) -> np.ndarray:
    subject_max = np.amax(scores, axis=0)

    return subject_max

#Input: scores: np.ndarray, start: int, end: int
#Output: np.ndarray (seçilen aralıktaki öğrencilerin puanları)
#Açıklama:
#Verilen başlangıç ve bitiş indexlerine göre öğrenci puanlarını dilimle. Belirli bir grup öğrenciye odaklanmak için kullanılır.
def slice_students_by_index(scores: np.ndarray, start: int, end: int) -> np.ndarray:
    arr = scores[start:end]
    return arr

#Input: scores: np.ndarray
#Output: 1D Numpy dizisi (her dersin standart sapması)
#Açıklama:
#scores dizisinin ne kadar dağıldığını görmek için standart sapma hesapla. Sapma, öğretim kalitesine dair ipuçları verebilir.
def calculate_subject_std(scores: np.ndarray) -> np.ndarray:
    std = np.std(scores, axis=0)
    return std

#Input: scores: np.ndarray
#Output: np.ndarray (0 ile 1 arası normalize edilmiş matris)
#Açıklama:
#Tüm puanları 0 ile 1 arasına ölçekle. Böylece büyü gücü açısından karşılaştırmalı analizler yapılabilir.
def normalize_scores(scores: np.ndarray) -> np.ndarray:
    min_val = np.min(scores)
    max_val = np.max(scores)

    normalized_scores = (scores - min_val) / (max_val - min_val)
    
    return normalized_scores
