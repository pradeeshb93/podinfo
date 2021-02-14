from kubernetes import client, config
from flask import Flask,jsonify
pod = {}
pod_res = []
app = Flask(__name__)
@app.route("/")

def trigger_refresh_cache():
    # it works only if this script is run by K8s as a POD
    config.load_kube_config()

    v1 = client.CoreV1Api()
    ret = v1.list_pod_for_all_namespaces(label_selector='app=podinfoapp1')
    for i in ret.items:
    	pod[i.metadata.name] = i.status.pod_ip
    for k in pod:
    	pod_res.append( {
		"POD_IP": pod[k],
		"POD_NAME": k
		})
    	return jsonify(pod_res)
       # print("%s\t%s\t%s" %
       #       (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
