import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(config_path="./configs", config_name='config')
def main(config: DictConfig):
    from train import train

    print(OmegaConf.to_yaml(config))

    train(config)


if __name__ == "__main__":
    main()
