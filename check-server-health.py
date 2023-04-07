import psutil
import shutil

def check_cpu_usage(interval = 1):
    return psutil.cpu_percent(interval)

def check_mem_usage():
    resume = psutil.virtual_memory()
    return resume.percent

def check_hard_disk_free_space(partition = '/'):
    total , used , free = shutil.disk_usage(partition)
    return round((used * 100) / total,2)

print('CPU USAGE : {} %'.format(check_cpu_usage()))
print('USAGE HARD DISK : {} %'.format(check_hard_disk_free_space()))
print('USED MEMORY: {} %'.format(check_mem_usage()))
