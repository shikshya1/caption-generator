config = {
	'images_path': '/content/drive/My Drive/ML-Project1/image-generator/train_val_data/Flicker8k_Dataset/', #Make sure you put that last slash(/)
	'train_data_path': '/content/drive/My Drive/ML-Project1/image-generator/train_val_data/Flickr_8k.trainImages.txt',
	'val_data_path': '/content/drive/My Drive/ML-Project1/image-generator/train_val_data/Flickr_8k.devImages.txt',
	'captions_path': '/content/drive/My Drive/ML-Project1/image-generator/train_val_data/Flickr8k.token.txt',
	'tokenizer_path': '/content/drive/My Drive/ML-Project1/image-generator/tokenizer.pkl',
	'model_data_path': '/content/drive/My Drive/ML Project/Image-Caption-Generator/model_data/', #Make sure you put that last slash(/)
	'model_load_path': '/content/drive/My Drive/ML Project/Image-Caption-Generator/model_data/model_inceptionv3_epoch-20_train_loss-2.4050_val_loss-3.0527.hdf5',
	'num_of_epochs': 1,
	'max_length': 40, #This is set manually after training of model and required for test.py
	'batch_size': 32,
	'beam_search_k':3,
	'test_data_path': '/content/drive/My Drive/ML-Project1/image-generator/test_data/', #Make sure you put that last slash(/)
	'model_type': 'inceptionv3', # inceptionv3 or vgg16
	'random_seed': 1035
}
