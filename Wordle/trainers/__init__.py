# Copied over from https://github.com/willccbb/verifiers/blob/main/verifiers/trainers/__init__.py

from .grpo_config import GRPOConfig
from .grpo_multiturn_trainer import GRPOMultiTurnTrainer
from peft import LoraConfig

def grpo_defaults(run_name: str) -> GRPOConfig:
    return GRPOConfig(
        output_dir=f"outputs/{run_name}",
        run_name=run_name,
        learning_rate=1e-6,
        lr_scheduler_type="constant_with_warmup",
        warmup_steps=10,
        num_train_epochs=1,
        max_grad_norm=2.0,
        gradient_checkpointing=True,
        save_strategy="steps",
        save_steps=500,
        save_only_model=True,
        logging_steps=1,
        log_on_each_node=False,
        log_completions=True,
    )

def lora_defaults(r = 8, alpha = 16) -> LoraConfig:
    return LoraConfig(
        r=r,
        lora_alpha=alpha,
        target_modules=["q_proj", "v_proj", "k_proj", "o_proj"],
        task_type="CAUSAL_LM",
    )

__all__ = ["GRPOConfig", "GRPOMultiTurnTrainer", "grpo_defaults", "lora_defaults"]