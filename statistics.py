class Statistics:
    """Класс для статистических вычислений"""
    
    def mean(self, numbers):
        """Вычисляет среднее значение"""
        return sum(numbers) / len(numbers) if numbers else 0
    
    def median(self, numbers):
        """Вычисляет медиану"""
        sorted_nums = sorted(numbers)
        n = len(sorted_nums)
        if n % 2 == 0:
            return (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
        else:
            return sorted_nums[n//2]
    
    def describe(self, numbers):
        """Выводит описание набора данных"""
        return {
            'mean': self.mean(numbers),
            'median': self.median(numbers),
            'count': len(numbers),
            'min': min(numbers) if numbers else 0,
            'max': max(numbers) if numbers else 0
        }