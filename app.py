from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/trigger', methods=['POST'])
def trigger():
    # 从请求中提取 JSON 数据
    data = request.get_json()

    start = data.get("start_location")
    end = data.get("end_location")
    time = data.get("departure_time")

    # 模拟处理逻辑
    response = {
        "status": "success",
        "message": f"行程从 {start} 到 {end}，出发时间：{time}"
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run()
