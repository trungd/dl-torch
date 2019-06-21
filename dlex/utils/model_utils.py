"""Model utils"""

import json
import os


def load_results(params):
    """Load all saved results at each checkpoint."""
    path = os.path.join(params.log_dir, "results.json")
    if os.path.exists(path):
        with open(os.path.join(params.log_dir, "results.json")) as f:
            return json.load(f)
    else:
        return {
            "best_results": {},
            "evaluations": []
        }


def add_result(params, new_result):
    """Add a checkpoint for evaluation result."""
    ret = load_results(params)
    ret["evaluations"].append(new_result)
    for m in params.metrics:
        if m not in ret["best_results"] or \
                new_result['result'][m] > ret['best_results'][m]['result'][m]:
            ret["best_results"][m] = new_result
    with open(os.path.join(params.log_dir, "results.json"), "w") as f:
        f.write(json.dumps(ret, indent=4))
    return ret["best_results"]