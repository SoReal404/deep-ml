import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:


	if mode == "column":
		result = []
		matrix = np.array(matrix)
		for col in range(matrix.shape[1]):
			result.append(np.mean(matrix[:, col]))
			
		return result

	elif mode =="row":
		result = []
		matrix = np.array(matrix)
		for row in range(matrix.shape[0]):
			result.append(np.mean(matrix[row, :]))

		return result