from ray import serve
from ray.serve.llm import LLMConfig, build_openai_app

llm_config = LLMConfig(
    model_loading_config=dict(
        model_id="tinyllama-1.1b",  # your name for the deployment
        model_source="TinyLlama/TinyLlama-1.1B-Chat-v1.0",  # HF repo
    ),
    deployment_config=dict(
        autoscaling_config=dict(
            min_replicas=1,
            max_replicas=1,
        ),
        # Optional: per-replica resource requests
        ray_actor_options={
            "num_cpus": 1,
            "num_gpus": 1,  # each replica gets 1 GPU
        },

    ),
    # accelerator_type="T4",   # tells Ray to place it on a T4 node if available
    log_engine_metrics=True,
)

app = build_openai_app({"llm_configs": [llm_config]})
serve.run(app, blocking=True)
