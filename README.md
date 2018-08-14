# Python-WangyiTokenCollectCoinScript
网易星球黑钻自动领取脚本

# 详情
[开发过程碎碎念](https://www.jianshu.com/p/62b5c64e2dc1)

# 备注
该脚本仅供学习使用

# Build docker image

```
docker build -t star:0.1.0 .
```

# K8S CronJob
```yaml
apiVersion: batch/v1beta1
kind: CronJob
metadata:
  name: star
spec:
  schedule: "0 11 * * *"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: star
            image: star:0.1.0
            imagePullPolicy: Always
            env:
            - name: NTES_YD_SESS
              value:
            - name: GA
              value:
            - name: STAREIG
              value:
          restartPolicy: Never
```