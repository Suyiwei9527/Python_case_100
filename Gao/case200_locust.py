import os
from locust import task, TaskSet, HttpUser, constant
 
 
# 任务集 用户行为脚本
class UserBehavior(TaskSet):
 
    @task(1)
    def getBasicProfile(self):
        # headers根据自己的接口实际情况填写即可
        headers = {'content-type': 'application/x-www-form-urlencoded',
                   'ua': 'xxx',
                   'Cookie': 'xxx',
                   }
        url = "http://192.168.101.75:80/gao.php"
        res = self.client.get(url, headers=headers)
        #print(res.json())
    wait_time = constant(1)  # 每个用户在每次任务执行之间等待5秒
 
 
class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    min_wait = 500
    max_wait = 1000
    #host = "http://192.168.101.75:80,http://192.168.101.78:80"
 
if __name__ == "__main__":
    os.system("locust -f %s -P 8089" % __file__)   # 此处导入os，可以在pycharm中直接运行此py文件