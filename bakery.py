from metaflow import pypi, FlowSpec, step, kubernetes, conda

class BakeryBenchmark(FlowSpec):

    @step
    def start(self):
        raise Exception("stop")
        self.next(self.end)

  
    

    """
    @pypi(
        python="3.12",
        packages={
            "xgboost": "2.1.1",
            "numpy": "2.1.1",
            "pandas": "2.2.3"
        },
    )
    """
    """
    @pypi(
        python="3.10.11",
        packages={
            "vllm": "0.6.1",
            "transformers": "4.44.2",
            "huggingface-hub": "0.25.1",
        },
    )
    """
    """
    @pypi(
        python="3.12",
        packages={
            "faiss-cpu": ">=1.7.2",
            "datasets": "3.1.0",
            "psutil": ">=5.9.1",
            "torch": ">=1.11.0",
            "pytorch-lightning": "2.4.0",
            "nvidia-ml-py": "12.560.30",
            "ray": ">=1.13.0"
        }
    )
    """
    """
    @conda(
        python="3.12",
        packages={
            "selenium": "4.26.1",
            "geckodriver": "0.35.0",
            "firefox": "132.0",
            "bokeh": "3.6.0",
            "glib": "2.82.2"
        }
    )
    """
    @pypi(
        python="3.9",
        packages={
            "numpy": ">=1.17.3",
            "pillow": ">=7.0.0",
            "sentencepiece": ">=0.1.91",
            "flatbuffers": ">=2.0",
            "absl-py": ">=0.10.0",
            "urllib3": ">=1.21.1",
            "tflite-support": ">=0.4.2",
            "tensorflowjs": ">=2.4.0",
            "tensorflow": ">=2.6.0",
            "numba": ">=0.53",
            "librosa": "0.8.1",
            "lxml": ">=4.6.1",
            "matplotlib": ">=3.0.3",
            "six": ">=1.12.0",
            "tensorflow-model-optimization": ">=0.5"
        }
    )
    @kubernetes
    @step
    def end(self):
        pass

if __name__ == '__main__':
    BakeryBenchmark()
