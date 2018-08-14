FROM golang:1.9.4-alpine3.7 as builder
WORKDIR /go/src/star
COPY . .
RUN go build .

FROM python:alpine3.7
RUN pip3 install requests
WORKDIR /
COPY --from=builder /go/src/star .
COPY WangYiCoin.py .
CMD ["./star"]
