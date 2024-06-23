from typing import List


def recall_at_k(labels: List[int], scores: List[float], k=5) -> float:
    """Recall calculation"""
    sorted_indices = sorted(range(len(scores)), key=lambda i:scores[i], reverse=True)
    top_k_indices = sorted_indices[:k]
    tp = sum([labels[i] == 1 for i in top_k_indices])
    total_positives = sum(labels)
    return tp / total_positives if total_positives > 0 else 0.0


def precision_at_k(labels: List[int], scores: List[float], k=5) -> float:
    """Precision calculation"""
    sorted_indices = sorted(range(len(scores)), key=lambda i:scores[i], reverse=True)
    top_k_indices = sorted_indices[:k]
    correct_predictions = sum(labels[i] for i in top_k_indices)
    precision = correct_predictions / k
    return precision


def specificity_at_k(labels: List[int], scores: List[float], k=5) -> float:
    """Specificity calculation"""
    sorted_labels = [label for _, label in sorted(zip(scores, labels), reverse=True)]
    top_k_labels = sorted_labels[:k]
    true_negatives = sum(1 for label in top_k_labels if label == 0)
    actual_negatives = sum(1 for label in labels if label == 0)
    if actual_negatives == 0:
        return 0.0
    else:
        return true_negatives / actual_negatives


def f1_at_k(labels: List[int], scores: List[float], k=5) -> float:
    """F1 score calculation"""
    sorted_indices = sorted(range(len(scores)), key=lambda i:scores[i], reverse=True)
    top_k_indices = sorted_indices[:k]
    correct_predictions = sum(labels[i] for i in top_k_indices)
    precision = correct_predictions / k
    total_positives = sum(labels)
    recall = correct_predictions / total_positives
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
    return f1